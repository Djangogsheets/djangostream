import streamlit as st
import pandas as pd
#import os
#print("Current working directory:", os.getcwd())

# Load the CSV file
csv_file_path = '123.csv'
data = pd.read_csv(csv_file_path)

# Streamlit app
st.title("TYRES 123 POS report ")
st.write("Here's the data for the POS:")

# Display the data
st.dataframe(data)
#st.tabulator(data)