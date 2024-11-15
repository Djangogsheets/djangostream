import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

# Set up the Streamlit page configuration
#st.set_page_config(page_icon="🌴", page_title="Tabulator表格", layout="wide")

# Upload CSV file
#file = st.file_uploader("请上传文件", type=["csv"])
file = '123.csv'

if file is not None:
    df = pd.read_csv(file, encoding="gbk")

    # Calculate totals for cash and card
    total_cash = df['cash'].sum() if 'cash' in df.columns else 0
    total_card = df['card'].sum() if 'card' in df.columns else 0

    def draw_table(df, height, width):
        columns = df.columns
        column_selection = []
        column_selection.append("""<select id="filter-field" style="font-size:15px;background:white;color:black;border-radius:15%;border-color:grey;">""")
        for col in columns:
            column_selection.append(f"""<option value='{col}'>{col}</option>""")
        column_selection.append("""</select>""")

        # Add date filter for date_creation if it exists
        if 'date_creation' in columns:
            column_selection.append("""<input id="filter-date" type="date" style="font-size:15px;border-color:grey;border-radius:5%;">""")

        table_data = df.to_dict(orient="records")
        column_setting = []
        column_setting.append("""{rowHandle:true, formatter:"handle", headerSort:false, frozen:true, width:30, minWidth:30}""")
        for col in columns:
            column_setting.append(f"""{{"title":"{col}", "field":"{col}", "width":200, "sorter":"string", "hozAlign":"center", "headerFilter":"input", "editor": "input"}}""")

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
            <div style="margin-left:30%;">
                {''.join(column_selection)}
                <input id="filter-value" type="text" placeholder="填写要筛选的内容" style="font-size:15px;border-color:grey;border-radius:5%">
                <button id="filter-clear" style="font-size:15px;background:#00ccff;color:white;border-radius:15%;border-color:white;">清除筛选</button>
            </div>
            <div style="margin-left:30%; margin-top:10px;">
                <strong>总现金: {total_cash}</strong><br>
                <strong>总卡片: {total_card}</strong>
            </div>
            <div id="example-table"></div>
            <script type="text/javascript">
                var tabledata = {table_data};
                var table = new Tabulator("#example-table", {{
                    height: {height},
                    data: tabledata,
                    layout: "fitDataTable",
                    movableRows: true,
                    resizableColumnFit: true,
                    pagination: "local",
                    paginationSize: 5,
                    tooltips: true,
                    columns: [{', '.join(column_setting)}],
                }});

                document.getElementById("filter-clear").addEventListener("click", function() {{
                    table.clearFilter();
                }});

                // Add event listener for date filter
                document.getElementById("filter-date").addEventListener("change", function() {{
                    var dateValue = this.value;
                    if (dateValue) {{
                        table.setFilter("date_creation", "=", dateValue);
                    }} else {{
                        table.clearFilter("date_creation");
                    }}
                }});
            </script>
        </body>
        </html>
        """, height=height, width=width)

    draw_table(df, 500, 1200)

else:
    # Load the default CSV file if no file is uploaded
    csv_file_path = '123.csv'
    data = pd.read_csv(csv_file_path)

    # Streamlit app
    st.title("TYRES  POS report ")
    st.write("Here's the data for the POS:")

    # Display the data
    st.dataframe(data)