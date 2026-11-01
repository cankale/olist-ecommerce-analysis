import pandas as pd 
import seaborn as sns

df = pd.read_csv('data/raw/olist_orders_dataset.csv')

print(df.isna().sum())

print(df.columns)

