# 🛢️ Alberta Oil Production Dashboard

🖥️ [Click here to explore the Alberta Oil Dashboard](https://alberta-oil-dashboard.onrender.com)

<img src="media/demo.gif" width="700"/>

---

## Table of Contents

* [Production Overview](#production-overview)
* [Historical Trends](#historical-trends)
* [Distribution](#distribution)
* [Rolling Avg Analysis](#rolling-avg-analysis)
* [Forecasting](#forecasting)
* [Data Insights](#data-insights)
* [About](#about)
* [Social Media](#social-media)

---

## Production Overview

This section summarizes Alberta’s **crude oil production performance** over the past year. It highlights:

- **Total Production** (monthly output)
- **Year-over-Year Change**
- **Monthly Growth**
- **Cumulative Production**

A line graph illustrates monthly production trends, including key fluctuations like the early 2024 dip and recent recovery. Real-time data is pulled via Alberta’s open API and dynamically calculated to give users a live, accurate snapshot of the province's production status.

---

## Historical Trends

This section visualizes oil production in Alberta from 2006 to 2025 using an interactive line chart. Key insights include:

- A steady long-term upward trend
- Production declines around 2016–2017
- Post-2020 recovery and growth

Users can zoom, hover, and pan through this timeline to explore how events such as price crashes and policy shifts impacted Alberta’s production trajectory.

---

## Distribution

Explore the **distribution of monthly crude oil output** using a histogram that reveals:

- A multimodal distribution pattern
- Clusters likely linked to market demand, regulations, or extraction methods
- A shift toward higher-volume clusters over time

This visualization may reflect Alberta’s growing reliance on bitumen and synthetic production alongside conventional sources.

---

## Rolling Avg Analysis

This section applies a **12-month rolling average** to monthly production data to:

- Smooth short-term noise
- Clarify underlying trends
- Highlight periods of volatility or steady growth

The red line represents the rolling mean, revealing long-term structural patterns that are often missed in raw time-series data.

---

## Forecasting

Two models are used to predict Alberta’s future crude oil production into 2026:

- **Simple Linear Regression**  
  A trend-based model capturing broad growth direction.

- **ARIMA (AutoRegressive Integrated Moving Average)**  
  A time series model that accounts for lag, trend, and seasonality. It shows a mild production plateau, with confidence intervals highlighting future uncertainty.

These forecasts help contextualize Alberta’s oil trajectory under different modeling assumptions.

---

## Data Insights

This section dives deeper into production behavior using:

- **Exponential Decline Curve**  
  A reservoir-engineering model showing natural production drop-off over time due to resource depletion and aging infrastructure.

- **Correlation Heatmap**  
  Visualizes relationships between:
  - **Total vs Non-Conventional**: Strong correlation, indicating high reliance
  - **Total vs Conventional**: Moderate correlation
  - **Conventional vs Non-Conventional**: Lower correlation, showing distinct behavior patterns

These tools collectively reveal Alberta’s increasing dependence on non-conventional crude sources like bitumen and synthetic oil.

---

## About

### 📊 Project Overview

This dashboard was developed to visualize and forecast Alberta’s **crude oil production**, including **conventional crude, bitumen, and synthetic crude**, using real-time government data.

🔧 **Built With**:
- Python, Flask
- HTML, CSS/SCSS, JavaScript, Bootstrap
- Plotly for interactive charts
- SQLite for local data management
- Prototyped in MATLAB, developed in Visual Studio

📡 **Live Data Source**:
- Government of Alberta’s public [API](https://economicdashboard.alberta.ca/dashboard/oil-production)
- Volt Flask Dashboard template by Creative Tim

🧠 **Features**:
- KPI visualizations
- ARIMA and linear regression forecasts
- Decline curve modeling
- Real-time API updates

The dashboard aims to combine clarity, interactivity, and industry relevance through data storytelling.

---

### 👩‍💻 About Me – Zinab Bin Sumait

**Aspiring Energy & Data Analyst**

This project is my first full-stack technical build. I began coding in **January 2025** with the mission of turning energy data into actionable insights.

🎓 I completed an *Introduction to the Oil & Gas Industry* course at **Mount Royal University** in **December 2024**, and hold a **BComm in International Business Strategy** from the **University of Calgary (June 2024)**.

> My work lives at the intersection of **energy, economics, and emerging tech**, and I’m passionate about supporting informed, data-driven decisions in Alberta’s resource sector.

[View My Resume](#) <!-- Replace this with your real resume link -->

---

## Social Media

- 🔗 [LinkedIn: linkedin.com/in/zinab-b-886865201](https://www.linkedin.com/in/zinab-b-886865201)

---

© 2025 Zinab Bin Sumait – All Rights Reserved.
