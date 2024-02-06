import streamlit as st

st.header("Activities")

st.selectbox("Choose an activity.",
             ['Soccer', 'Basketball', 'Tennis', 'Golf', 'Volleyball', 'Baseball'],
             index=None,
             placeholder="Please select one")

