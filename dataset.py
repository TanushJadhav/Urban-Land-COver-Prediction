import streamlit as st
import pandas as pd

df = pd.read_csv('training.csv')
st.dataframe(df)
