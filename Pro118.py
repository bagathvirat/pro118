import pandas as pd
import plotly.express as px

df = pd.read_csv("stars.csv")

print(df.head())

fig = px.scatter(df, x="Size", y="Light")
fig.show()