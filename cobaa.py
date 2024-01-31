import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Header
st.header('Sarmila Yetria :sparkles:')
st.subheader ('Plot')

x = np.linspace(-2 * np.pi, 2 * np.pi, 1000) 
y = np.sin (x) # calculating sin (x) values
z = np.scos (x) # calculating cos (x) values

fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(x, y, label='sin(x)', color='b') #plotting sin(x) curve 
ax.plot(x, z , label='cos(x)', color='g') #plotting cods(x) curve 
ax.set_ylabel("")
ax.set_xlabel("x")
ax.tick_params(axis='y', labelsize=20)
ax.set_xticklabels(ax.get_sticklabels(), rotation =20, ha='right')
ax.tick_params(axis='x', labelsize=15)

st.pyplot(fig)
