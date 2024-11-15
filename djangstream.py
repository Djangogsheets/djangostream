import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
import os

# Set up the Streamlit page configuration
st.set_page_config(page_icon=" ", page_title="POS Report", layout="wide")

# Load the default CSV file
file = '123.csv'

# Check if the file exists
if os.path.exists(file):
    df = pd.read_csv(file, encoding="gbk")

    # Debug: Display the DataFrame
    st.title('POS Report')
    st.dataframe(df)

    # Draw the table
    def draw_table(df, height, width):
        columns = df.columns
        table_data = df.to_dict(orient="records")
        column_setting = []
        column_setting.append("""{rowHandle:true, formatter:"handle", headerSort:false, frozen:true, width:30, minWidth:30}""")
        for col in columns:
            column_setting.append(f"""{{"title":"{col}", "field":"{col}", "width":200, "sorter":"string", "hozAlign":"center", "headerFilter":"input", "editor": "input"}}""")

        # custom max min filter function
        
        function minMaxFilterFunction(headerValue, rowValue, rowData, filterParams) {
            //headerValue - the value of the header filter element
            //rowValue - the value of the column in this row
            //rowData - the data for the row being filtered
            //filterParams - params object passed to the headerFilterFuncParams property

            if (rowValue) {
                if (headerValue.start != "") {
                    if (headerValue.end != "") {
                        return rowValue >= headerValue.start && rowValue <= headerValue.end;
                    } else {
                        return rowValue >= headerValue.start;
                    }
                } else {
                    if (headerValue.end != "") {
                        return rowValue <= headerValue.end;
                    }
                }
            }
            return true; //must return a boolean, true if it passes the filter.
        }
        
        # custom max min header filter
        
        var minMaxFilterEditor = function(cell, onRendered, success, cancel, editorParams){
            var end;
            var container = document.createElement("span");
            //create and style inputs
            var start = document.createElement("input");
            start.setAttribute("type", "number");
            start.setAttribute("placeholder", "Min");
            start.setAttribute("min", 0);
            start.setAttribute("max", 100);
            start.style.padding = "4px";
            start.style.width = "50%";
            start.style.boxSizing = "border-box";
            start.value = cell.getValue();

            function buildValues(){
                success({
                    start:start.value,
                    end:end.value,
                });
            }

            function keypress(e){
                if(e.keyCode == 13){
                    buildValues();
                }

                if(e.keyCode == 27){
                    cancel();
                }
            }

            end = start.cloneNode();
            end.setAttribute("placeholder", "Max");

            start.addEventListener("change", buildValues);
            start.addEventListener("blur", buildValues);
            start.addEventListener("keydown", keypress);

            end.addEventListener("change", buildValues);
            end.addEventListener("blur", buildValues);
            end.addEventListener("keydown", keypress);

            container.appendChild(start);
            container.appendChild(end);

            return container;
        }
        

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
                    
                    headerFilterFunc:minMaxFilterFunction,
                    headerFilterLiveFilter:false,
                    headerFilterEditor:minMaxFilterEditor,
                }});
            </script>
        </body>
        </html>
        """, height=height, width=width)

    draw_table(df, 500, 1200)

else:
    st.title("Error")
    st.write(f"The file '{file}' does not exist. Please ensure it is located in the correct directory.")

