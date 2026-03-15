import streamlit as st
import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

plt.rcParams["font.family"] = "DejaVu Sans"


data= pd.read_csv('/Users/asif/Documents/Gen ai /Python/matlib.py/Chocolate Sales (2).csv')

data['Amount'] = data['Amount'].replace('[\$,]', '', regex=True).astype(float)

st.title('Sales Data Dashboard')

st.write('Dataset preview')
st.dataframe(data)

data['Date'] = pd.to_datetime(data['Date'], dayfirst=True)
data['Months']= data['Date'].dt.month_name()

total_sales = data['Amount'].sum()
st.metric('Total Revenue', total_sales)


top_product = data.groupby('Product')['Amount'].sum().sort_values(ascending= False).head(10)
country_sale = data.groupby('Country')['Amount'].sum().sort_values(ascending=False).head(10)
monthly_sale = data.groupby('Months')['Amount'].sum().sort_values(ascending=False).head(10)
best_sales = data.groupby('Sales Person')['Amount'].sum().sort_values(ascending=False).head(10)


fig1, ax1 = plt.subplots(figsize=(8,5)) 
sns.histplot(data['Amount'],bins=30, ax= ax1)
ax1.set_title('Revenue distribution')
plt.tight_layout()
ax1.tick_params(axis='x', rotation=45)
st.pyplot(fig1)
plt.close(fig1)

fig2, ax2 = plt.subplots(figsize=(8,5))
sns.barplot(x=top_product.index, y=top_product.values, ax=ax2)
ax2.set_title('Revenue as per product')
plt.tight_layout()
ax2.tick_params(axis='x', rotation=45)
st.pyplot(fig2)
plt.close(fig2)

fig3, ax3 = plt.subplots(figsize=(8,5))
sns.barplot(x=country_sale.index,y=country_sale.values,ax=ax3)
ax3.set_title('Revenue as per country')
plt.tight_layout()
ax3.tick_params(axis='x', rotation=45)
st.pyplot(fig3)
plt.close(fig3)

fig4, ax4 = plt.subplots(figsize=(8,5))
sns.barplot(x=monthly_sale.index,y=monthly_sale.values,ax=ax4)
ax4.set_title('Monthly sales')
plt.tight_layout()
ax4.tick_params(axis='x', rotation=45)
st.pyplot(fig4)
plt.close(fig4)

fig5, ax5 = plt.subplots(figsize=(8,5))
sns.barplot(x=best_sales.index,y=best_sales.values,ax=ax5)
ax5.set_title('Best sales person')
plt.tight_layout()
ax5.tick_params(axis='x', rotation=45)
st.pyplot(fig5)
plt.close(fig5)


