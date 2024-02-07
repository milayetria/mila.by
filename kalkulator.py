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
    y = st.number_input('Angka ',value=1)

# Operasi matematika
with st.expander('Hasil');
if operator == '+':
    result = x + y 
    elif operator == '-':
    result = x - y 
    elif operator == 'x':
    result = x * y 
    elif operator == ':':
if y != 0:
    result = x / y 
    result = x  y 
else 
result = "Pembagian dengan nol tidak bisa"

st.write(f'Hasil dari {x}  {operator} {y} adalah {result}')

st.caption('Copyright © Sarmila Yetria 2024')
