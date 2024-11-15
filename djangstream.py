import streamlit as st
import pandas as pd
import os

# Set up the Streamlit page configuration
st.set_page_config(page_icon="🌴", page_title="POS Report", layout="wide")

# Load the default CSV file
file = '123.csv'

# Check if the file exists
if os.path.exists(file):
    df = pd.read_csv(file, encoding="gbk")

    # Display the title
    st.title("POS Report")
    
    # Create filters for each column
    for column in df.columns:
        if df[column].dtype == 'object':  # For string columns
            unique_values = df[column].unique()
            selected_values = st.multiselect(f"Filter by {column}", options=unique_values, default=unique_values)
            if selected_values:
                df = df[df[column].isin(selected_values)]
        elif df[column].dtype == 'number':  # For numeric columns
            min_value = float(df[column].min())
            max_value = float(df[column].max())
            selected_range = st.slider(f"Select range for {column}", min_value=min_value, max_value=max_value, value=(min_value, max_value))
            df = df[(df[column] >= selected_range[0]) & (df[column] <= selected_range[1])]
        elif df[column].dtype == 'datetime64[ns]':  # For date columns
            unique_dates = df[column].dt.date.unique()  # Get unique dates
            selected_date = st.selectbox(f"Select date for {column}", options=unique_dates)
            df = df[df[column].dt.date == selected_date]  # Filter by selected date

    # Display the filtered DataFrame
    st.dataframe(df)

else:
    st.title("Error")
    st.write(f"The file '{file}' does not exist. Please ensure it is located in the correct directory.")