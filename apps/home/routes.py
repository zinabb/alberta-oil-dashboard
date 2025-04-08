# THIS IS apps/home/routes.py

from flask import redirect, url_for, render_template, request, Response
from apps.home import blueprint
from flask_login import login_required
from jinja2 import TemplateNotFound
import matplotlib
matplotlib.use("Agg")

import pandas as pd
import numpy as np
import requests

# New imports for Plotly
import plotly.express as px
import plotly.offline as pyo
import plotly.graph_objects as go

# Other necessary imports
from sklearn.linear_model import LinearRegression
from statsmodels.tsa.arima.model import ARIMA
from calendar import monthrange

@blueprint.route('/index')
def index():
    return render_template('home/index.html', segment='index')

@blueprint.route('/<template>')
@login_required
def route_template(template):
    try:
        if not template.endswith('.html'):
            template += '.html'
        segment = get_segment(request)
        return render_template("home/" + template, segment=segment)
    except TemplateNotFound:
        return render_template('home/page-404.html'), 404
    except:
        return render_template('home/page-500.html'), 500

def get_segment(request):
    try:
        segment = request.path.split('/')[-1]
        if segment == '':
            segment = 'index'
        return segment
    except:
        return None

### --- Interactive Graph Routes --- ###

# Utility: Fetch Alberta Total Oil Data from the live API
def fetch_oil_data():
    url = "https://api.economicdata.alberta.ca/api/data?code=b0881da3-704c-42b9-a429-c8eff0ec5c73"
    response = requests.get(url)
    json_data = response.json()  # list of records
    df = pd.DataFrame(json_data)
    df['Date'] = pd.to_datetime(df['Date'])

    return df

# Utility: Fetch Alberta Oil Data Type from Live API
def fetch_oil_type_breakdown():
    url = "https://api.economicdata.alberta.ca/api/data?code=3caa6978-9647-4eb3-8de8-34a3abc06427"
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame(data)
    df['Date'] = pd.to_datetime(df['Date'])
    return df

# Graph 1: Alberta’s Total Oil Production Over Time (Interactive)
@blueprint.route("/graph1")
def graph1():

    df = fetch_oil_data()

    fig = go.Figure()

    # Add the production line trace
    fig.add_trace(go.Scatter(x=df['Date'], y=df['Value'],
                          mode='lines', name='Production'))

    # Add vertical shaded region (from 2016-01-01 to 2017-01-01)
    fig.add_shape(type="rect",
        xref="x", yref="paper",
        x0="2016-01-01", x1="2017-01-01",
        y0=0, y1=1,
        fillcolor="gray", opacity=0.3, layer="below", line_width=0)

    # Add annotation (using sample indices similar to your matplotlib code)
    annot_x = df['Date'].iloc[112] if len(df) > 112 else df['Date'].iloc[-1]
    annot_y = df['Value'].iloc[50] if len(df) > 50 else df['Value'].iloc[0]
    fig.add_annotation(x=annot_x,
                    y=annot_y,
                    text="Peak Decline",
                    showarrow=True,
                    arrowhead=2,
                    ax=0,
                    ay=10)

    # Update layout
    fig.update_layout(title={
                        'text': "Alberta's Total Oil Production Over Time",
                        'x':0.5,
                        'xanchor': 'center'},
                   xaxis_title="Date (year)",
                   yaxis_title="Production (barrels/day)",
                   font=dict(size=14),
                   template="plotly_white")
    ##fig.show()
    graph_div = pyo.plot(fig, output_type="div", include_plotlyjs=True)
    return render_template("home/graph_template.html", graph_div=graph_div)

# Graph 2: Histogram of Production Values
@blueprint.route("/graph2")
def graph2():
    df = fetch_oil_data()
    fig = px.histogram(
        df, 
        x="Value", 
        nbins=30, 
        title="Distribution of Production Values",
        labels={"Production": "Production (barrels/day)"}
    )

    fig.update_traces(marker=dict(line=dict(width=1, color="navy")))

    graph_div = pyo.plot(fig, output_type="div", include_plotlyjs=True)
    return render_template("home/graph_template.html", graph_div=graph_div)

# Graph 3: Rolling Average Production
@blueprint.route("/graph3")
def graph3():
    df = fetch_oil_data()
   
    df["RollingMean"] = df["Value"].rolling(window=12).mean()
    fig3 = go.Figure()
    fig3.add_trace(go.Scatter(x=df['Date'], y=df['Value'],
                          mode='lines', name='Actual Production', opacity=0.5))
    fig3.add_trace(go.Scatter(x=df['Date'], y=df['RollingMean'],
                          mode='lines', name='12-Month Rolling Mean', line=dict(color='red')))
    fig3.update_layout(title="Production with Rolling Mean",
                   xaxis_title="Date",
                   yaxis_title="Production",
                   font=dict(size=14),
                   template="plotly_white")

    graph_div = pyo.plot(fig3, output_type="div", include_plotlyjs=True)
    return render_template("home/graph_template.html", graph_div=graph_div)

# Graph 4: Simple Linear Regression Forecast (Next 12 Months)
@blueprint.route("/graph4")
def graph4():
    df = fetch_oil_data()
    df["Date_Ordinal"] = df["Date"].map(pd.Timestamp.toordinal)
    X = df[["Date_Ordinal"]]
    y = df["Value"]
    model = LinearRegression()
    model.fit(X, y)
    future_dates = pd.date_range(df["Date"].max(), periods=13, freq='M')[1:]
    future_ordinal = np.array([d.toordinal() for d in future_dates]).reshape(-1,1)
    predictions = model.predict(future_ordinal)

    fig4 = go.Figure()
    # Historical data trace
    fig4.add_trace(go.Scatter(x=df['Date'], y=df['Value'],
                          mode='lines', name='Historical Data', line=dict(color='teal')))
    # Forecast trace
    fig4.add_trace(go.Scatter(x=future_dates, y=predictions,
                          mode='lines', name='Forecast', line=dict(color='magenta', dash='dash')))
    fig4.update_layout(title="Simple Linear Regression Forecast",
                   xaxis_title="Date",
                   yaxis_title="Production",
                   font=dict(size=14),
                   template="plotly_white")

    graph_div = pyo.plot(fig4, output_type="div", include_plotlyjs=True)
    return render_template("home/graph_template.html", graph_div=graph_div)

# Graph 5: ARIMA Future Forecasting
@blueprint.route("/graph5")
def graph5():
    df = fetch_oil_data()
  

    df_arima = pd.DataFrame({
    'Date': pd.date_range(start='2020-01-01', periods=36, freq='M'),
    'Production': [1000, 980, 960, 940, 900, 850, 800, 750, 720, 690, 670, 660, 
                   655, 645, 630, 620, 600, 590, 580, 570, 550, 530, 510, 500, 
                   495, 490, 485, 480, 470, 460, 450, 440, 430, 420, 410, 400]
})
    df_arima.set_index('Date', inplace=True)
    from statsmodels.tsa.arima.model import ARIMA

    # Fit ARIMA Model on historical production data
    model_arima = ARIMA(df_arima['Production'], order=(1, 1, 1))
    model_fit = model_arima.fit()

    forecast_steps = 48
    forecast_result = model_fit.get_forecast(steps=forecast_steps)
    forecast_values = forecast_result.predicted_mean
    conf_int = forecast_result.conf_int()

    # Create forecast dates
    forecast_dates = pd.date_range(start=df_arima.index[-1] + pd.DateOffset(months=1),
                               periods=forecast_steps, freq='M')

    fig5 = go.Figure()
    # Historical production trace
    fig5.add_trace(go.Scatter(x=df_arima.index, y=df_arima['Production'],
                          mode='markers+lines', name='Historical Production'))
    # Forecast trace
    fig5.add_trace(go.Scatter(x=forecast_dates, y=forecast_values,
                          mode='lines', name='Forecast', line=dict(color='red', dash='dash')))
    # Confidence interval filled area:
    x_fill = list(forecast_dates) + list(forecast_dates[::-1])
    y_fill = list(conf_int.iloc[:, 0]) + list(conf_int.iloc[:, 1][::-1])
    fig5.add_trace(go.Scatter(x=x_fill, y=y_fill,
                          fill="toself", fillcolor='pink', line=dict(color='rgba(255,255,255,0)'),
                          showlegend=True, name='Confidence Interval', opacity=0.3))
    fig5.update_layout(title="Crude Oil Production Forecast (ARIMA) into 2026",
                   xaxis_title="Date",
                   yaxis_title="Production (Barrels)",
                   font=dict(size=14),
                   template="plotly_white")
    graph_div = pyo.plot(fig5, output_type="div", include_plotlyjs=True)
    return render_template("home/graph_template.html", graph_div=graph_div)

# Graph 6: Exponential Decline Curve (Theoretical Model)
@blueprint.route("/graph6")
def graph6():
    time_vals = np.arange(0, 60, 1)
    qi = 1000
    di = 0.05
    production = qi * np.exp(-di * time_vals)
    fig = px.line(
        x=time_vals, 
        y=production, 
        title="Exponential Decline Curve",
        labels={"x": "Time (Months)", "y": "Production (Barrels)"}
    )
    graph_div = pyo.plot(fig, output_type="div", include_plotlyjs=True)
    return render_template("home/graph_template.html", graph_div=graph_div)

# Graph 7: Correlation Matrix
@blueprint.route("/graph7")
def graph7():
    # Fetch datasets
    df_total = fetch_oil_data()
    df_types = fetch_oil_type_breakdown()

    # Rename and pivot
    df_total = df_total.rename(columns={'Value': 'Total_Oil_Production'})
    df_types = df_types.pivot(index='Date', columns='Type', values='Value').reset_index()

    # Merge datasets
    merged = pd.merge(df_total[['Date', 'Total_Oil_Production']], df_types, on='Date', how='inner')
    
    # Keep relevant columns
    corr_df_all = merged[['Date', 'Total_Oil_Production', 'Conventional Oil', 'Non-Conventional Oil']].dropna()

    # Create a 'last 5 years' version
    cutoff_date = pd.to_datetime("today") - pd.DateOffset(years=5)
    corr_df_recent = corr_df_all[corr_df_all['Date'] >= cutoff_date]

    # Compute both correlation matrices
    corr_all = corr_df_all.drop(columns=['Date']).corr()
    corr_recent = corr_df_recent.drop(columns=['Date']).corr()

    # Create base heatmap
    fig = px.imshow(
        corr_all,
        text_auto=True,
        color_continuous_scale="RdBu_r",
        title="Correlation Matrix: All Time"
    )

    # Add dropdown menu
    fig.update_layout(
        updatemenus=[
            dict(
                buttons=[
                    dict(label="All Time",
                         method="update",
                         args=[
                             {"z": [corr_all.values], "x": corr_all.columns, "y": corr_all.index},
                             {"title": "Correlation Matrix: All Time"}
                         ]),
                    dict(label="Last 5 Years",
                         method="update",
                         args=[
                             {"z": [corr_recent.values], "x": corr_recent.columns, "y": corr_recent.index},
                             {"title": "Correlation Matrix: Last 5 Years"}
                         ])
                ],
                direction="down",
                showactive=True
            )
        ]
    )

    graph_div = pyo.plot(fig, output_type="div", include_plotlyjs=True)
    return render_template("home/graph_template.html", graph_div=graph_div)

# Additional Pages

# Production Overview FIRST GRAPH
@blueprint.route('/production-overview')
def production_overview():
    df = fetch_oil_data()
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values('Date')
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month

    # Get most recent record
    latest = df.iloc[-1]
    current_value = latest['Value']
    current_year = latest['Year']
    current_month = latest['Month']
    days_in_month = monthrange(current_year, current_month)[1]
    total_production_per_day = current_value / days_in_month

    # Get same month previous year (if it exists)
    prev_year_data = df[(df['Year'] == current_year - 1) & (df['Month'] == current_month)]
    yoy_change = None
    if not prev_year_data.empty:
        previous_value = prev_year_data.iloc[0]['Value']
        yoy_change = ((current_value - previous_value) / previous_value) * 100

    # Monthly growth
    previous_month_value = df.iloc[-2]['Value']
    monthly_growth = ((current_value - previous_month_value) / previous_month_value) * 100

    # Cumulative production
    cumulative_production = df['Value'].sum()

    # Format for frontend
    kpi_data = {
        'total_production': f"{round(total_production_per_day):,} barrels/day",
        'yoy_change': f"{round(yoy_change, 2)}%" if yoy_change is not None else "Data not available",
        'monthly_growth': f"{round(monthly_growth, 2)}%",
        'cumulative': f"{round(cumulative_production / 1_000_000, 2)} million barrels"
    }

    type_df = fetch_oil_type_breakdown()
    type_df = type_df.sort_values("Date")

    latest_date = type_df['Date'].max()
    previous_date = type_df['Date'].sort_values().unique()[-2]

    latest_df = type_df[type_df['Date'] == latest_date]
    prev_df = type_df[type_df['Date'] == previous_date]

    def get_value(df, oil_type):
        return df[df['Type'] == oil_type]['Value'].values[0] if oil_type in df['Type'].values else 0

    def pct_change(curr, prev):
        return round(((curr - prev) / prev) * 100, 2) if prev else 0

    def format_arrow(change_str):
        try:
            change = float(change_str.replace('%', '').strip())
            if change > 0:
                return f'<span style="color:green;">&#8593; {change_str}</span>'  # ↑
            elif change < 0:
                return f'<span style="color:red;">&#8595; {change_str}</span>'   # ↓
            else:
                return f'<span>{change_str}</span>'
        except:
            return f'<span>{change_str}</span>'

    oil_breakdown = {}
    for oil_type in ['Conventional Oil', 'Non-Conventional Oil', 'Total oil production']:
        curr_val = get_value(latest_df, oil_type)
        prev_val = get_value(prev_df, oil_type)

        oil_breakdown[oil_type] = {
            'production': f"{int(curr_val):,} b/d",
            'change': format_arrow(f"{pct_change(curr_val, prev_val)} %")
        }

    # Chart
    last_updated = latest['Date'].strftime("%B %Y")
    source = "Government of Alberta Economic Data"
    last_year = df[df['Date'] > (df['Date'].max() - pd.DateOffset(months=12))]
    fig = px.line(last_year, x="Date", y="Value", title="Production Trend (Last 12 Months)",
                  labels={"Production": "Production (b/d)"})
    mini_chart_div = pyo.plot(fig, output_type="div", include_plotlyjs=True)

    return render_template("home/production_overview.html",
                           kpi_data=kpi_data,
                           last_updated=last_updated,
                           source=source,
                           mini_chart_div=mini_chart_div,
                           oil_breakdown=oil_breakdown)

@blueprint.route('/historical-trends')
def historical_trends():
    return render_template('home/historical_trends.html')

@blueprint.route('/distribution')
def distribution():
    return render_template('home/distribution.html')

@blueprint.route('/rolling-avg')
def rolling_avg():
    return render_template('home/rolling_avg.html')

@blueprint.route('/forecasting')
def forecasting():
    return render_template('home/forecasting.html')

@blueprint.route('/data-insights')
def data_insights():
    return render_template('home/data_insights.html')

@blueprint.route('/about-the-project')
def about_the_project():
    return render_template("home/about_the_project.html")

@blueprint.route('/')
def home_redirect():
    return redirect(url_for('home_blueprint.production_overview'))

@blueprint.route("/test-fetch")
def test_fetch():
    df = fetch_oil_data()
    return "Columns in df: " + str(df.columns)






