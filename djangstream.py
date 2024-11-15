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

    # Ensure 'POS_date' is in datetime format
    if 'POS_date' in df.columns:
        df['POS_date'] = pd.to_datetime(df['POS_date'])

    # Display the title
    st.title("POS Report")

    # Create a sidebar for the date filter
    st.sidebar.header("Filter Options")
    
    # Create a dropdown to filter by POS_date in the sidebar
    unique_dates = df['POS_date'].dt.date.unique()  # Get unique dates
    selected_date = st.sidebar.selectbox("Select POS_date", options=unique_dates)

    # Filter the DataFrame based on the selected date
    filtered_df = df[df['POS_date'].dt.date == selected_date]

    # Calculate totals for cash and card
    total_cash = filtered_df['cash'].sum() if 'cash' in filtered_df.columns else 0
    total_card = filtered_df['card'].sum() if 'card' in filtered_df.columns else 0

    # Display the filtered DataFrame
    st.dataframe(filtered_df)

    # Display the totals
    st.subheader("Totals")
    st.write(f"Total Cash: ${total_cash:.2f}")
    st.write(f"Total Card: ${total_card:.2f}")

else:
    st.title("Error")
    st.write(f"The file '{file}' does not exist. Please ensure it is located in the correct directory.")