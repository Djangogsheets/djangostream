import subprocess
import datetime
import os
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components

def run_git_commands(repo_path):
    # Change to the specified repository directory
    os.chdir(repo_path)

    # Define the commit message with a timestamp
    commit_message = f"csv changed and {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

    try:
        # Add all changes
        subprocess.run(["git", "add", "."], check=True)
        print("Added changes to staging.")

        # Commit changes
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        print(f"Committed changes with message: '{commit_message}'")

        # Push to the main branch
        subprocess.run(["git", "push", "origin", "main"], check=True)
        print("Pushed changes to GitHub.")

    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

def load_data_and_draw_table():
    # Load the CSV file
    csv_file_path = '123.csv'  # Adjust this path if needed
    df = pd.read_csv(csv_file_path, encoding="gbk")

    # Calculate totals for cash and card
    total_cash = df['cash'].sum() if 'cash' in df.columns else 0
    total_card = df['card'].sum() if 'card' in df.columns else 0

    # Display the totals above the table
    st.write(f"**Total Cash: {total_cash}**")
    st.write(f"**Total Card: {total_card}**")

    # Draw the table
    draw_table(df)

def draw_table(df):
    # Prepare data for the table
    table_data = df.to_dict(orient="records")
    columns = df.columns.tolist()

    column_setting = []
    for col in columns:
        column_setting.append(f"""{{"title":"{col}", "field":"{col}", "width":200, "sortable":true}}""")

    components.html(f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Tabulator Example</title>
        <link href="https://unpkg.com/tabulator-tables@4.8.1/dist/css/tabulator_modern.min.css" rel="stylesheet">
        <script type="text/javascript" src="https://unpkg.com/tabulator-tables@4.8.1/dist/js/tabulator.min.js"></script>
    </head>
    <body>
        <div id="example-table"></div>
        <script type="text/javascript">
            var tabledata = {table_data};
            var table = new Tabulator("#example-table", {{
                height: "400px",
                data: tabledata,
                layout: "fitDataTable",
                pagination: "local",
                paginationSize: 5,
                columns: [{', '.join(column_setting)}],
            }});
        </script>
    </body>
    </html>
    """, height=500)

if __name__ == "__main__":
    # Specify the path to your Git repository
    repository_path = r"C:\JVCODE\DjangoGithub\djangostream"  # Use raw string for Windows path
    run_git_commands(repository_path)

    # Load data and draw table
    load_data_and_draw_table()