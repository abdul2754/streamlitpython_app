import streamlit as st
from pages import food_info
st.markdown(
    """<div style='text-align: center;'> 
    <h1>Swigy</h1> 
    <h3>Thank you for choosing Swigy</h3>
    <p>Please wait for some time.</p>
    </div>""",
    unsafe_allow_html=True
)

if "checkout_total" in st.session_state and "checkout_cart" in st.session_state:
    st.subheader("Your Cart:")
    for item, quantity in st.session_state.checkout_cart.items():
        st.write(f"{item}: {quantity} item(s)")

    st.subheader(f"Total Price: Rs. {st.session_state.checkout_total}")
else:
    st.warning("No items in your cart. Please go back to the food menu.")
