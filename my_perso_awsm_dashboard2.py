# Ignoring warning messages from python
import warnings
warnings.filterwarnings('ignore')

# General use imports
import pandas as pd
import numpy as np

# Visualization imports
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly
import plotly.express as px
import streamlit as st
import plost
from PIL import Image



# Modules and data
import requests
import acquire
import prep
from datetime import datetime
# import altair as alt

# Streamlit initial configuration and appearance( Page settings )
st.set_page_config(layout='wide')

with open('style2.css') as f:
    st.markdown(f"<style>'text-align: center;{f.read()}'</style>", unsafe_allow_html=True)

#Data
transactions = pd.read_csv('transactions.csv')
income = pd.read_csv('income.csv')
income_june = pd.read_csv('income_june.csv')
expenses = pd.read_csv('expenses.csv')
expenses_categories = pd.read_csv('expenses_categories.csv')
expenses_categories_june = pd.read_csv('expenses_categories_june.csv')
ttmi_graph = pd.read_csv('ttmi_graph.csv')
ttme_graph = pd.read_csv('ttme_graph.csv')

#Header
header = st.container()

with header:
    st.title('My Personal Financial Dashboard')

#Row A
ttm, current_month, ytd = st.columns(3)

with ttm:
    st.markdown('## TTM Income')
    st.markdown('(TTM = trailing 12 months)')
    plost.bar_chart(
        ttmi_graph,
        bar ='months',
        value ='amount',
        color='months',
        pan_zoom='minimap',
    )
    #fig = px.bar(ttmi_graph, x='months', y='amount', title='TTM Income', color='months', text_auto=True)
    #fig.update_layout(width=400,height=400, showlegend=False)    
    #st.write(fig)

with current_month:
    current_month.header('Current Month Income')
    st.metric(label= 'Total Income June', value='$5116.69', delta='$387.33', delta_color='normal')

with ytd:
    ytd.header('Types of Revenue')
    fig = px.pie(income, values='amount', names='category')
    fig.update_layout(width=400,height=300)
    st.write(fig, width=400,height=300)


    
#Row B
ttm2, topex, net = st.columns(3) 
    
with ttm2:
    ttm2.header('* TTM Expenses')
    plost.bar_chart(
        ttme_graph,
        bar ='category',
        value ='amount',
        color='category',
        pan_zoom='minimap',
    )
    #fig = px.bar(round(ttme_graph[1:8], 2), x='category', y='amount', title='TTM Expenses', color='category', text_auto=True)
    #fig.update_layout(width=400,height=400, showlegend=False)   
    #st.write(fig, '* TTM expenses table', round(ttme_graph[1:], 2), use_container_width=True)

with topex:
    topex.header('Top 7 June expenses by category')
    plost.donut_chart(
        data=expenses_categories,
        theta ='amount',
        color ='category',
        legend = 'right',
        use_container_width = True


    )

    #fig = px.bar(expenses_categories[1:8], x='category', y='amount', color="category", text_auto=True)
    #fig.update_layout(width=400,height=400, showlegend=False)
    #st.write(fig, use_container_width=True)

with net:
    net.header('Net income')
    net_income = (income_june).sum() - (expenses_categories_june.amount[1:]).sum()
    st.metric(label= 'Net Income June', value='806.17', delta=None, delta_color='normal')

#Row C
income2,vs, md = st.columns((4,2,4))

with income2:
    income2.header('Income')
    income2.markdown('* **Year to date total income**')
    ytd_income = pd.DataFrame(income.groupby('category', sort=False).amount.sum().sort_values(ascending=False))
    ytd_income1 = ytd_income.reset_index()
    fig = px.bar(ytd_income1, x="category", y="amount", color="category")
    fig.update_layout(width=400,height=400)
    st.write(fig, width=400,height=400)

with vs:
    vs.header('VS')


with md:
    md.header('Expenses')
    md.markdown('* **Year to date total expenses**')
    ytd_expenses = pd.DataFrame(expenses.groupby('category', sort=False).amount.sum().sort_values(ascending=False))
    ytd_expenses1 = ytd_expenses.reset_index()
    fig = px.bar(ytd_expenses1[1:8], x="category", y="amount", color="category")
    fig.update_layout(width=400,height=400)
    st.write(fig, width=400,height=400)

# /Users/arsen/codeup-data-science/personal_project/my_perso_awsm_dashboard.py