import plotly.express as px
import csv
import pandas as pd

df = pd.read_csv("project107Data.csv")

print(df.groupby("level")["attempt"].mean())

fig = px.scatter(x = df.groupby("level")["attempt"].mean(), y = ["Level 1","Level 2","Level 3","Level 4"],orientation = "h")

#fig.show()

df = pd.read_csv("project107Data.csv")
figure = px.scatter(df,x = "student_id",y = "level",color = "attempt", title = "Per Capita Income")
figure.show()