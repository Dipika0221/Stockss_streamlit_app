import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set Streamlit page config
st.set_page_config(page_title="Nifty Stock Visualizer", layout="wide")

# Load data
df = pd.read_csv("../DataSets/Nifty_Stocks.csv")

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Sidebar inputs
st.sidebar.title("Stock Filter")

# Unique categories
categories = df["Category"].unique()
selected_category = st.sidebar.selectbox("Select Category", categories)

# Filter symbols based on selected category
filtered_df = df[df["Category"] == selected_category]
symbols = filtered_df["Symbol"].unique()
selected_symbol = st.sidebar.selectbox("Select Symbol", symbols)

# Final filtered data
stock_data = filtered_df[filtered_df["Symbol"] == selected_symbol]

# Title
st.title("📈 Nifty Stock Price Visualization")
st.subheader(f"{selected_symbol} in {selected_category}")

# Line plot
plt.figure(figsize=(15, 6))
sns.lineplot(x=stock_data["Date"], y=stock_data["Close"])
plt.title(f"{selected_symbol} Closing Price Over Time")
plt.xlabel("Date")
plt.ylabel("Close Price")

# Display plot in Streamlit
st.pyplot(plt)
