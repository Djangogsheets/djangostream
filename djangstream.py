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

    # Display the DataFrame without any filters
    st.dataframe(df)

else:
    st.title("Error")
    st.write(f"The file '{file}' does not exist. Please ensure it is located in the correct directory.")