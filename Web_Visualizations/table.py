import pandas as pd
frame = pd.read_csv("images/cities.csv", index_col="City_ID")
html_table = frame.to_html("table.html")
html_table.replace('\n', '')