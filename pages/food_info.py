import streamlit as st
st.markdown(
        """<div style='text-align: center;'> 
        <h1>Swigy</h1> 
        <h3>Food details</h3>
        </div>""",
        unsafe_allow_html=True
    )

menu = [
        {"name": "Pizza", "description": "Delicious cheesy pizza", "price": 200, "image": "https://img.lovepik.com/free-png/20210919/lovepik-pizza-png-image_400594998_wh1200.png"},
        {"name": "Burger", "description": "Juicy beef burger", "price": 250, "image": "https://img.pikbest.com/origin/10/12/46/10fpIkbEsTkIQ.png!bw700"},
        {"name": "Salad", "description": "Fresh green salad", "price": 50, "image": "https://static.vecteezy.com/system/resources/thumbnails/046/437/566/small_2x/mix-salad-transparent-background-png.png"},
        {"name": "Sushi", "description": "Authentic Japanese sushi", "price": 150, "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSMYWrpsTCR9mYD79mfk8NGG85fszD0LXhauw&s"},
        {"name": "Pasta", "description": "Hydrabadi Biriyani", "price": 250, "image": "https://images.rawpixel.com/image_png_800/cHJpdmF0ZS9sci9pbWFnZXMvd2Vic2l0ZS8yMDI0LTA4L3Jhd3BpeGVsX29mZmljZV8yMl9waG90b2dyYXBoX29mX2NoaWNrZW5fZHVtX2JpcnlhbmlfX3NpbmdsZV9wbl81ZTU4YjQ0My1lNmNhLTQ1ZDMtYWFhNC1jNmE4YzY4MTg3ZmEucG5n.png"},
        {"name": "Juice", "description": "Mix fruit juice", "price": 75, "image": "https://img.pikbest.com/png-images/20240604/-mix-fruit-juice_10598608.png!w700wp"}
]

if 'cart' not in st.session_state:
    st.session_state.cart = {}
    st.session_state.total_price = 0    
    
for i in range(0, len(menu), 2):
    cols = st.columns(2)
    for col, item in zip(cols, menu[i:i+2]):
        with col:
            st.image(item["image"], use_container_width=True)
            st.header(item["name"])
            st.write(item["description"])
            st.write(f"Price: Rs. {item['price']}")
            if st.button(f"Add {item['name']} to cart"):
                if item["name"] in st.session_state.cart:
                    st.session_state.cart[item["name"]] += 1
                else:
                    st.session_state.cart[item["name"]] = 1
                st.session_state.total_price += item["price"]
                st.success(f"Added {item['name']} to cart")

if st.button("Proceed to Checkout"):
    st.write(f"**Please pay the amount of Rs. {st.session_state.total_price}**")
    st.session_state.checkout_total = st.session_state.total_price 
    st.session_state.checkout_cart = st.session_state.cart
    st.switch_page("./pages/checkout.py")