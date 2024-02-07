import streamlit as st

# Header 
st.header('Sarmila Yetria:sparkles:')
st.subheader('Plot')

c1, c2, c3 = st.columns(3)

with c1:
    x = st.number_input('Angka ',value=100)
    st.write('=>: ')
with c2:
    operator = st.selectbox(
        'Operator',
        ('+', '-', 'x', ':'), key='k1')
    st.write(':sparkles: ')
with c3:
    x = st.number_input('Angka ',value=100)

st.write(x, '',operator,' = ','')

st.caption('Copyright © Sarmila Yetria 2023')
