import streamlit as st
import pandas as pd

def save_user_details(fn,ln,email,phone):
    data = {
        'First name' : [fn],
        'Last name ' : [ln],
        'email' : [email],
        'phone' : [phone],
    }
    df = pd.DataFrame(data)
    file_name = f"{fn}_{ln}_savings.csv"
    df.to_csv(file_name, index = False)
    st.success("Data saved successfully")
st.markdown( """<div style='text-align: center;'> <h1>Savings Details</h1> </div>""", unsafe_allow_html=True ) 
fn, ln = st.columns(2) 
first_name = fn.text_input("First name") 
last_name = ln.text_input("Last name") 
email, phone = st.columns([3, 1]) 
email_input = email.text_input("Email") 
phone_input = phone.text_input("Phone number") 

if st.button("Submit"): 
    if first_name and last_name: 
        save_user_details(first_name, last_name, email_input, phone_input)
        