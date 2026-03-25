# walmart-sales

This repository contains a Streamlit-based web application designed to visualize and analyze Walmart sales performance. The dashboard provides an interactive way to explore store-level data, including sales distribution, performance comparisons, and statistical spreads.
## Key Features

    Sales Distribution: An interactive donut chart showing how sales are distributed across different stores.

    Performance Analysis: Bar charts to compare total weekly sales by store.

    Statistical Insights: Box plots to visualize the data spread, outliers, and variance for each store.

    Data Preview: A snapshot of the first 10 rows of the raw dataset for quick inspection.

    Dataset Integration: Direct links and code snippets to download the source data via Kaggle.

## Project Structure

    dashboard.py: The main Python script containing the Streamlit configuration and visualization logic.

    Walmart_Sales.csv: The source dataset (ensure this is in the root directory).

    Walmart-Logo.png: Visual branding for the dashboard header.

## Prerequisites

Before running the application, ensure you have the following Python libraries installed:

    Streamlit: For the web interface.

    Pandas: For data manipulation.

    Plotly: For interactive visualizations.

Bash

pip install streamlit pandas plotly

## How to Run

    Clone this repository or download the dashboard.py file.

    Place the Walmart_Sales.csv and Walmart-Logo.png files in the same folder as the script.

    Open your terminal and run:
    Bash

    streamlit run dashboard.py

## Dataset Information

The data used in this project is sourced from the Walmart Sales dataset available on Kaggle. It includes information such as:

    Store Number: Unique identifier for each store.

    Weekly Sales: The recorded sales amount for a specific week.
