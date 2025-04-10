# Alberta Crude Oil Production

<img src="media/demo.gif" width="700"/>

<br />

## Table of Contents

* [Production Overview](#production-overview)
* [Historical Trends](#historical-trends)
* [Distribution](#distribution)
* [Rolling Avg Analysis](#rolling-avg-analysis)
* [Forecasting](#forecasting)
* [Data Insights](#data-insights)
* [About](#about)

<br />

## Production Overview

> The Production Overview section summarizes Alberta’s crude oil performance over the past year. It highlights key metrics like:
>
> - **Total Production** (monthly output)
> - **Year-over-Year Change**
> - **Monthly Growth**
> - **Cumulative Production**
>
> A line graph shows monthly trends, revealing fluctuations in output—such as the production drop in early 2024 and subsequent recovery. This real-time data is fetched via API and calculated dynamically to give decision-makers a clear snapshot of the province's production status.

<br />

## Historical Trends

> This section visualizes Alberta’s oil production from 2006 to 2025. The interactive line chart highlights:
>
> - A steady upward trend in oil production over the past two decades
> - A **peak decline** around 2016–2017
> - Resilient recovery post-2020 and continuing upward momentum
>
> Users can zoom and pan through the timeline, making it easy to explore how external events (e.g., oil price crashes, policy changes) influenced Alberta’s production levels.

<br />

## Distribution

> This part of the dashboard explores the **distribution of monthly production volumes**, offering insight into how oil output varies over time.
>
> The histogram reveals a **multimodal distribution**, with notable clustering. These peaks likely reflect differing production intensities tied to market demand, regulatory changes, or extraction strategy. The shift toward higher production clusters may indicate improvements in operational efficiency or reliance on non-conventional methods.

<br />

## Rolling Avg Analysis

> This section presents a 12-month **Rolling Average Line** overlaid on top of the actual monthly production data.

The rolling average smooths short-term fluctuations and highlights broader trends over time. This makes it easier to observe:
- Long-term production growth
- Periods of volatility or decline
- Structural changes in Alberta’s oil output

The red line represents the **12-month rolling mean**, offering a clearer picture of underlying trends compared to the more jagged raw data in blue. This type of analysis is commonly used in energy analytics to reduce noise and improve the readability of time-series performance.

<br />

## Forecasting 

> This section includes two forecasting models to project Alberta's crude oil production trends into 2026:

- **Simple Linear Regression**  
  A straightforward trendline that projects future production based on historical growth. While effective at capturing long-term direction, it may overlook volatility.

- **ARIMA Forecast**  
  A more advanced time series model incorporating lag, trend, and seasonality. The ARIMA model predicts a slight production plateau, with its shaded confidence interval capturing uncertainty due to market and operational fluctuations.

> These models are valuable for comparing different forecasting perspectives and understanding future planning scenarios.

<br />

## Data Insights 

> This section features an **Exponential Decline Curve** and a **Correlation Heatmap**, both designed to offer deeper insights into Alberta’s crude oil production dynamics.

- **Exponential Decline Curve**  
  A standard tool in reservoir engineering, this model visualizes the natural decline in production rates over time. It reflects diminishing output due to resource depletion or aging infrastructure, providing a realistic outlook on long-term production behavior.

- **Correlation Matrix**  
  The heatmap quantifies the strength of relationships between:
  - **Total vs Non-Conventional**: High correlation, indicating Alberta’s heavy dependence on non-conventional sources.
  - **Total vs Conventional**: Moderate correlation, showing a smaller but consistent influence.
  - **Conventional vs Non-Conventional**: Weaker correlation, suggesting distinct production patterns between the two types.

> Together, these tools highlight Alberta’s growing reliance on non-conventional oil and offer actionable insights for policymakers, analysts, and energy strategists seeking to support balanced and resilient production systems.

---

## About

### 📊 Project Overview

This dashboard was developed to visualize and forecast Alberta’s crude oil production trends using real-time government data.

🔧 **Built With**:  
- **Python**, Flask  
- **HTML**, **CSS/SCSS**, **JavaScript**, **Bootstrap**  
- **Plotly** for interactive charts  
- Prototyped in **MATLAB**, transitioned to a full-stack web app in **Visual Studio**

📡 **Live Data Source**:  
- Government of Alberta’s public API
- Used Volt Flask by Creative Tim for template guidance

🔍 **Features**:
- Key performance indicators (KPIs)
- Correlation analysis
- Forecasting models (Linear Regression, ARIMA)
- Industry-specific visuals (e.g., Exponential Decline Curve)

The layout prioritizes clarity, interactivity, and policy relevance—designed with modern data storytelling in mind.

---

### 👩‍💻 About Me – Zinab Bin Sumait  
**Aspiring Energy & Data Analyst**

This dashboard is my first full-stack technical project, and it represents a meaningful step in my journey. I began coding in **January 2025** with the goal of turning energy data into actionable insights.

🎓 After completing an *Introduction to the Oil & Gas Industry* course at **Mount Royal University** in **December 2024**, I was inspired to explore Alberta’s energy sector from a data-driven lens.

📈 With a **Bachelor of Commerce in International Business Strategy** from the **University of Calgary (June 2024)**, I bring a foundation in strategy — now combined with analytics.

> My work lives at the intersection of **economics, energy, and technology** —  
> and I'm committed to supporting informed, data-driven decision-making in Alberta’s resource sector.

[View My Resume](#) <!-- Replace with your actual resume link -->

---

<br />

## Social Media

- LinkedIn: [www.linkedin.com/in/zinab-b-886865201](https://www.linkedin.com/in/zinab-b-886865201)

<br />

---

Zinab Bin Sumait - All Rights Reserved.
