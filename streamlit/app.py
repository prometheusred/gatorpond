import streamlit as st
import pandas as pd
import psycopg2

st.title("🏀 UF Athletics Data Dashboard")

try:
    conn = psycopg2.connect(
        host="",
        dbname="",
        user="",
        password=""
    )
    df = pd.read_sql("SELECT NOW() as current_time", conn)
    st.write("Connected to Postgres!", df)
except Exception as e:
    st.error(f"Postgres connection failed: {e}")
