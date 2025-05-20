import streamlit as st

st.title("Hello Streamlit!")
st.write("This is a simple Streamlit app.")


st.header('st.button')

if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')
