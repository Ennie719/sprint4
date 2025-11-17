import pandas as pd
import streamlit as st
import plotly.express as px
df = pd.read_csv('../vehicles_us.csv')
# fig = px.histogram(df, x='price',
#                     title='Distribution of Car Prices',
#                     labels={'price': 'Price ($)','count':'Number of Cars'})
# fig.show()
print("Dataset shape:", df.shape)
print("/nColumn names:")
print(df.columns.tolist())

df.head()