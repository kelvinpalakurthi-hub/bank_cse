import streamlit as st
import pandas as pd
from supabase import create_client

#supabase config

SUPABASE_URL="https://jerlqbchngploqrjjsuv.supabase.co"
SUPABASE_KEY="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImplcmxxYmNobmdwbG9xcmpqc3V2Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjYwNDA4MTYsImV4cCI6MjA4MTYxNjgxNn0.FO6uIgLyRVC_Tp00Yzdf94bWgJwzbsx77yCfdIIi-rQ"
supabase=create_client(SUPABASE_URL,SUPABASE_KEY)

#Streamlit UI

st.title("HDFC BANK (supabase)")
menu=["REGISTER","VIEW"]
choice=st.sidebar.selectbox("Menu",menu)

#Register

if choice == "REGISTER":
    name=st.text_input("Enter name")
    age=st.number_input("Age",min_value=18)
    account=int(st.number_input("ACCOUNT NUMBER"))
    balance=st.number_input("BALANCE",min_value=500)
    if st.button("SAVE"):
        supabase.table("users").insert({"name": name,"age": age,"account": account,
                                        "balance": balance}).execute()
        st.success("User added succesfully ")

#view students

if choice =="VIEW":
    st.subheader("view users")
    data=supabase.table("users").select("*").execute()
    df=pd.DataFrame(data.data)
    st.dataframe(df)
