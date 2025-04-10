# Alberta Crude Oil Production

![Demo](media/zinabvid.gif)

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

This dashboard was developed as a data visualization and forecasting tool to analyze Alberta’s crude oil production trends.  

Built using **Microsoft Visual Studio**, the project utilizes:
- **Python** as the core language  
- **HTML**, **CSS/SCSS**, **JavaScript**, **Bootstrap**, and **Plotly** for frontend design  
- Early prototyping in **MATLAB**, later transitioned into a fully interactive Flask web app  

📡 **Real-time data** is sourced from the **Government of Alberta’s public API**, ensuring the insights reflect the latest available data.  
The dashboard includes:
- Key KPIs
- Correlation matrices
- Forecasting models (Simple Linear Regression, ARIMA)
- Domain-specific visuals like the Exponential Decline Curve

The layout follows a clean, modular design with a strong emphasis on clarity, usability, and data storytelling.

---

### 👩‍💻 Zinab Bin Sumait  
**Aspiring Energy and Data Analyst **  

This dashboard represents both a **personal milestone** and a **professional foundation**. I started coding in **January 2025**, sparked by a desire to bring economic and energy data to life.

After completing an *Introduction to the Oil and Gas Industry* course at **Mount Royal University** in **December 2024**, I developed this project to explore Alberta’s vital role in global energy.

🛠️ This dashboard is my **first technical project**, built entirely through self-learning and passion for energy analytics.

> This work bridges strategy, data science, and energy.  
> My goal is to grow at the intersection of **economics, energy, and technology**, and contribute meaningfully to Alberta’s evolving energy sector.

[View My Resume](#) <!-- Replace with actual link if you'd like -->

---

<br />

## Social Media

- LinkedIn: [www.linkedin.com/in/zinab-b-886865201](https://www.linkedin.com/in/zinab-b-886865201)

<br />

---

Zinab Bin Sumait - All Rights Reserved.
