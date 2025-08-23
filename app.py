import streamlit as st
from utils import df

st.set_page_config(layout='wide')

st.title("Atividade 3 - Credit Card Spending in India (Dashboard)")
st.write("Link: https://www.kaggle.com/datasets/divyaraj2006/credit-card-spending-in-india")
st.image("assets/course_banner.png")

st.write(df.head())