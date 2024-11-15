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

    # Debug: Display the DataFrame
    st.title("POS Report")
    st.write("POS Report loaded successfully:")

    # Create filters for each column
    for column in df.columns:
        if df[column].dtype == 'object':  # For string columns, use a selectbox or multiselect
            unique_values = df[column].unique()
            selected_values = st.multiselect(f"Filter by {column}", options=unique_values, default=unique_values)
            df = df[df[column].isin(selected_values)]
        elif df[column].dtype == 'number':  # For numeric columns, use a slider
            min_value = float(df[column].min())
            max_value = float(df[column].max())
            selected_range = st.slider(f"Filter by {column}", min_value=min_value, max_value=max_value, value=(min_value, max_value))
            df = df[(df[column] >= selected_range[0]) & (df[column] <= selected_range[1])]
        elif df[column].dtype == 'datetime64[ns]':  # For date columns, use date input
            start_date = df[column].min().date()
            end_date = df[column].max().date()
            selected_dates = st.date_input(f"Filter by {column}", [start_date, end_date])
            df = df[(df[column] >= pd.to_datetime(selected_dates[0])) & (df[column] <= pd.to_datetime(selected_dates[1]))]

    # Display the filtered DataFrame
    st.dataframe(df)

else:
    st.title("Error")
    st.write(f"The file '{file}' does not exist. Please ensure it is located in the correct directory.")