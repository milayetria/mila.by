import streamlit as st

# Header 
st.header('Sarmila :sparkles:')
st.subheader('Plot')

c1, c2 = st.columns(2)

with c1:
    x = st.number_input('Angka ',value=100)
    st.write('=>: ')
with c2:
    operator = st.selectbox(
        'Operator',
        ('+', '-', 'x', ':'), key='k1')
    st.write(':sparkles: ')

st.write(x, '',operator,' = ','')

st.caption('Copyright © Sarmila Yetria 2023')
