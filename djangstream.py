import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
import os

# Set up the Streamlit page configuration
st.set_page_config(page_icon="🌴", page_title="POS Report", layout="wide")

# Load the default CSV file
file = '123.csv'

# Check if the file exists
if os.path.exists(file):
    df = pd.read_csv(file, encoding="gbk")

    # Debug: Display the DataFrame
    st.title('POS Report')
    # st.write("Data loaded successfully:")
    st.dataframe(df)


    # Define variables for input elements
    field_el = document.getElementById("filter-field")
    type_el = document.getElementById("filter-type")
    value_el = document.getElementById("filter-value")
def custom_filter(data):
    return data['car'] and data['rating'] < 3

def update_filter():
  filter_val = field_el.options[field_el.selectedIndex].value
  type_val = type_el.options[type_el.selectedIndex].value

  filter_func = custom_filter if filter_val == "function" else filter_val

  if filter_val == "function":
      type_el.disabled = True
      value_el.disabled = True
  else:
      type_el.disabled = False
      value_el.disabled = False

  if filter_val:
      table.setFilter(filter_func, type_val, value_el.value)

#//Update filters on value change
document.getElementById("filter-field").addEventListener("change", updateFilter);
document.getElementById("filter-type").addEventListener("change", updateFilter);
document.getElementById("filter-value").addEventListener("keyup", updateFilter);

#//Clear filters on "Clear Filters" button click
document.getElementById("filter-clear").addEventListener("click", function(){
  field_el.value = "";
  type_el.value = "=";
  value_el.value = "";
  table.clearFilter();
});

table.clearFilter();






    def draw_table(df, height, width):
        columns = df.columns
        column_selection = []
        # column_selection.append("""<select id="filter-field" style="font-size:15px;background:white;color:black;border-radius:15%;border-color:grey;">""")
        for col in columns:
            column_selection.append(f"""<option value='{col}'>{col}</option>""")
        column_selection.append("""</select>""")

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
            <div>
  <select id="filter-field">
    <option></option>
    <option value="ref">ref</option>
    
  </select>

  <select id="filter-type">
    <option value="=">=</option>
    <option value="<"><</option>
    <option value="<="><=</option>
    <option value=">">></option>
    <option value=">=">>=</option>
    <option value="!=">!=</option>
    <option value="like">like</option>
  </select>

  <input id="filter-value" type="text" placeholder="value to filter">

  <button id="filter-clear">Clear Filter</button>
</div>

<div id="example-table"></div>






            <div id="example-table"></div>
            <script type="text/javascript">
                var tabledata = {table_data};
                var table = new Tabulator("#example-table", {{
                    height: {height},
                    data: tabledata,
                    layout: "fitDataTable",
                    movableRows: true,
                    movableColumns:true,
                    resizableColumnFit: true,
                    pagination: "local",
                    paginationSize: 5,
                    tooltips: true,
                    columns: [{', '.join(column_setting)}],
                    
                }});
            </script>
        </body>
        </html>
        """, height=height, width=width)

    draw_table(df, 500, 1200)

else:
    st.title("Error")
    st.write(f"The file '{file}' does not exist. Please ensure it is located in the correct directory.")