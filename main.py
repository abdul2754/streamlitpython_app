import streamlit as st
import time 
def main():
    st.markdown(
        """ <div style = 'text-align : center;'>
        <h1>swigy</h1>
        <h3>have a great day with swigy</h3>
        </div>
        """, unsafe_allow_html = True
    )
    st.image("https://images.moneycontrol.com/static-mcnews/2018/02/Swiggy.jpg?impolicy=website&width=1600&height=900",use_container_width=True)
    st.markdown(
        """ <div style = 'text-align : center;'>
        <h3><i>How can I help you Today!!!</i></h3>
        </div>
        """, unsafe_allow_html = True
    )
    time.sleep(5)
    st.switch_page("./pages/customer_info.py")
    
if __name__ == '__main__':
    main()    
