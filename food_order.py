import streamlit as st
import pandas as pd

if 'page' not in st.session_state:
    st.session_state.page = 'starting'


def save_user_details(fn,ln,email,phone,ads):
    data = {
        'First name' : [fn],
        'Last name ' : [ln],
        'email' : [email],
        'phone' : [phone],
        'Address' : [ads]
    }
    df = pd.DataFrame(data)
    file_name = f"{fn}_{ln}_order_details.csv"
    df.to_csv(file_name, index = False)
    st.session_state.page = 'next'
    st.success("Data saved successfully")
    
def next_page():
    st.title("Next Page")
    st.write("Hello abdul")    
def starting_page():   
    st.markdown( """<div style='text-align: center;'> <h1>Swigy</h1> </div>""", unsafe_allow_html=True ) 
    fn, ln = st.columns(2) 
    first_name = fn.text_input("First name") 
    last_name = ln.text_input("Last name") 
    email, phone = st.columns([3, 1]) 
    email_input = email.text_input("Email") 
    phone_input = phone.text_input("Phone number") 
    ads = st.text_input("Address")

    if st.button("Submit"): 
        if first_name and last_name: 
            save_user_details(first_name, last_name, email_input, phone_input,ads)
        
        else:
            st.error("Enter you First name and Last name") 


if page == 'starting':
    starting_page()          
elif page == 'next':   
    next_page()   
               