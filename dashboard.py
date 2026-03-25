import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard",layout="centered")
st.title("Walmart Sales Dashboard")
st.markdown("<h1 style='color:red:'font-size:24px;'>Welcome to the Walmart Sales Dashboard! Explore the sales data and gain insights into store performance.</h1>", unsafe_allow_html=True)
st.image("Walmart-Logo.png")
df = pd.read_csv("Walmart_Sales.csv")
st.subheader("Sales Distribution")
fig1=px.pie(df,names="Store",values="Weekly_Sales",hole=0.4)
st.plotly_chart(fig1)
st.subheader("Sales Performance")
fig2=px.bar(df,x="Store",y="Weekly_Sales",color="Store")
st.plotly_chart(fig2)
st.subheader("Data Spread")
fig3=px.box(df,x="Store",y="Weekly_Sales",color="Store")
st.plotly_chart(fig3)
st.subheader("Data preview")
st.write(df.head(10))
st.link_button("dataset link","https://www.kaggle.com/datasets/mikhail1681/walmart-sales")
st.code("""import kagglehub

# Download latest version
path = kagglehub.dataset_download("mikhail1681/walmart-sales")

print("Path to dataset files:", path)""", language="python")