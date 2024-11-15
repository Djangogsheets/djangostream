import streamlit as st
import pandas as pd

# Load the CSV file
csv_file_path = '123.csv'  # Adjust the path if necessary
data = pd.read_csv(csv_file_path)

# Streamlit app
st.title("My Streamlit App with CSV Data")
st.write("Here's the data from the CSV file:")

# Display the data
st.dataframe(data)
