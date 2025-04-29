import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import warnings

# Filter out warnings
warnings.filterwarnings("ignore")

# App configuration
st.set_page_config(
    page_title="Business Analytics Dashboard",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sample data generation
@st.cache_data
def generate_sales_data():
    dates = pd.date_range(start="2023-01-01", end="2024-12-31")
    products = ['Product A', 'Product B', 'Product C', 'Product D']
    regions = ['North', 'South', 'East', 'West']
    
    data = {
        'Date': np.random.choice(dates, 1000),
        'Product': np.random.choice(products, 1000),
        'Region': np.random.choice(regions, 1000),
        'Sales': np.random.randint(50, 500, 1000),
        'Profit': np.random.uniform(10, 200, 1000).round(2)
    }
    df = pd.DataFrame(data)
    df['Date'] = pd.to_datetime(df['Date'])
    return df

@st.cache_data
def generate_kpi_data():
    months = pd.date_range(start="2023-01-01", periods=12, freq='M')
    return pd.DataFrame({
        'Month': months,
        'Revenue': (np.random.normal(100, 20, 12).cumsum() * 1000).astype(int),
        'Customers': np.random.randint(500, 1500, 12),
        'Expenses': (np.random.normal(30, 5, 12).cumsum() * 1000).astype(int)
    })

# Navigation
def navigation():
    st.sidebar.title("Business Dashboard")
    st.sidebar.markdown("---")
    page = st.sidebar.radio(
        "Navigate",
        ["Sales Overview", "Product Analysis", "Regional Performance", "Financial Metrics"],
        label_visibility="collapsed"
    )
    st.sidebar.markdown("---")
    st.sidebar.markdown("### About")
    st.sidebar.info(
        "Interactive business analytics dashboard for tracking key performance indicators."
    )
    return page

# Page 1: Sales Overview
def sales_overview():
    st.title("📊 Sales Overview")
    st.markdown("High-level sales performance metrics and trends")
    
    df = generate_sales_data()
    kpi_df = generate_kpi_data()
    
    # KPI Cards
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Sales", f"${df['Sales'].sum():,}")
    with col2:
        st.metric("Average Profit", f"${df['Profit'].mean():.2f}")
    with col3:
        st.metric("Unique Products", df['Product'].nunique())
    with col4:
        st.metric("Regions Covered", df['Region'].nunique())
    
    st.markdown("---")
    
    # Time period selection
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start Date", 
                                 value=datetime(2023, 1, 1),
                                 min_value=datetime(2023, 1, 1),
                                 max_value=datetime(2024, 12, 31))
    with col2:
        end_date = st.date_input("End Date",
                               value=datetime(2024, 12, 31),
                               min_value=datetime(2023, 1, 1),
                               max_value=datetime(2024, 12, 31))
    
    # Filter data
    filtered_df = df[(df['Date'].dt.date >= start_date) & 
                    (df['Date'].dt.date <= end_date)]
    
    st.markdown("---")
    
    # Sales trend
    st.subheader("Sales Trend Over Time")
    trend_df = filtered_df.groupby(pd.Grouper(key='Date', freq='M'))['Sales'].sum().reset_index()
    fig = px.line(trend_df, x='Date', y='Sales', 
                 title="Monthly Sales Trend",
                 markers=True)
    st.plotly_chart(fig, use_container_width=True)
    
    # Revenue vs Expenses
    st.subheader("Revenue vs Expenses")
    fig = px.bar(kpi_df, x='Month', y=['Revenue', 'Expenses'],
                barmode='group',
                title="Monthly Financial Performance")
    st.plotly_chart(fig, use_container_width=True)

# Page 2: Product Analysis
def product_analysis():
    st.title("📦 Product Analysis")
    st.markdown("Performance metrics by product category")
    
    df = generate_sales_data()
    
    # Product selection
    selected_products = st.multiselect(
        "Select Products to Analyze",
        options=df['Product'].unique(),
        default=df['Product'].unique()
    )
    
    if not selected_products:
        st.warning("Please select at least one product")
        return
    
    filtered_df = df[df['Product'].isin(selected_products)]
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Sales by Product")
        sales_by_product = filtered_df.groupby('Product')['Sales'].sum().reset_index()
        fig = px.pie(sales_by_product, names='Product', values='Sales',
                    title="Sales Distribution by Product")
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Profit Margins")
        profit_by_product = filtered_df.groupby('Product')['Profit'].mean().reset_index()
        fig = px.bar(profit_by_product, x='Product', y='Profit',
                    title="Average Profit by Product")
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    # Product trend over time
    st.subheader("Product Performance Over Time")
    product_trend = filtered_df.groupby(['Product', pd.Grouper(key='Date', freq='M')])['Sales'].sum().reset_index()
    
    fig = px.line(product_trend, x='Date', y='Sales', color='Product',
                 title="Monthly Sales by Product",
                 markers=True)
    st.plotly_chart(fig, use_container_width=True)

# Page 3: Regional Performance
def regional_performance():
    st.title("🌍 Regional Performance")
    st.markdown("Sales and profit metrics by geographic region")
    
    df = generate_sales_data()
    
    # Map visualization (simulated)
    st.subheader("Regional Sales Distribution")
    
    # Create simulated geo data
    regions = df['Region'].unique()
    region_coords = {
        'North': [40.7128, -74.0060],
        'South': [34.0522, -118.2437],
        'East': [25.7617, -80.1918],
        'West': [47.6062, -122.3321]
    }
    
    region_df = pd.DataFrame({
        'Region': regions,
        'Sales': df.groupby('Region')['Sales'].sum().values,
        'Lat': [region_coords[r][0] for r in regions],
        'Lon': [region_coords[r][1] for r in regions]
    })
    
    fig = px.scatter_geo(region_df, lat='Lat', lon='Lon',
                        size='Sales',
                        hover_name='Region',
                        projection="natural earth",
                        title="Sales by Region")
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Sales by Region")
        fig = px.bar(df.groupby('Region')['Sales'].sum().reset_index(),
                    x='Region', y='Sales',
                    title="Total Sales by Region")
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Profit by Region")
        fig = px.box(df, x='Region', y='Profit',
                    title="Profit Distribution by Region")
        st.plotly_chart(fig, use_container_width=True)

# Page 4: Financial Metrics
def financial_metrics():
    st.title("💰 Financial Metrics")
    st.markdown("Key financial indicators and performance")
    
    kpi_df = generate_kpi_data()
    
    # Financial KPI Cards
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Revenue", f"${kpi_df['Revenue'].sum():,}")
    with col2:
        st.metric("Total Expenses", f"${kpi_df['Expenses'].sum():,}")
    with col3:
        profit = kpi_df['Revenue'].sum() - kpi_df['Expenses'].sum()
        st.metric("Net Profit", f"${profit:,}")
    
    st.markdown("---")
    
    # Revenue vs Expenses trend
    st.subheader("Revenue vs Expenses Trend")
    fig = px.line(kpi_df, x='Month', y=['Revenue', 'Expenses'],
                 title="Monthly Financial Performance",
                 markers=True)
    st.plotly_chart(fig, use_container_width=True)
    
    # Profit margin calculation
    kpi_df['Profit'] = kpi_df['Revenue'] - kpi_df['Expenses']
    kpi_df['Margin'] = (kpi_df['Profit'] / kpi_df['Revenue']) * 100
    
    st.subheader("Profit Margin Trend")
    fig = px.line(kpi_df, x='Month', y='Margin',
                 title="Monthly Profit Margin (%)",
                 markers=True)
    fig.update_yaxes(ticksuffix="%")
    st.plotly_chart(fig, use_container_width=True)
    
    # Customer metrics
    st.subheader("Customer Acquisition")
    fig = px.area(kpi_df, x='Month', y='Customers',
                 title="Monthly Active Customers")
    st.plotly_chart(fig, use_container_width=True)

# Main app logic
def main():
    page = navigation()
    
    if page == "Sales Overview":
        sales_overview()
    elif page == "Product Analysis":
        product_analysis()
    elif page == "Regional Performance":
        regional_performance()
    elif page == "Financial Metrics":
        financial_metrics()

if __name__ == "__main__":
    main()
