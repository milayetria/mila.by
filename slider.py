import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

x = st.slider('Pilih rentang', -3.0, 3.0, (.2, .5))
st.write('nilai x:', x)
y = st.slider('Set nilai', 0.0, 100.0, 25.0)
st.write('nilai y:', y)

t = np.linspace(x[0]*np.pi,x[1]*np.pi,100)
u = np.sin(t)
#st.write('nilai t:', t)

fig, ax = plt.subplots(figsize=(16,8))
ax.plot(t, u, label='sin(t)', color='b') 
ax.set_ylabel("")
ax.set_xlabel("t")
ax.tick_params(axis='y', labelsize=20)
ax.set_xticklabels(ax.get_xticklabels(), rotation=30, ha='right')
ax.tick_params(axis='x', labelsize=15)
plt.grid(color='green', linestyle='-.', linewidth=.5)
st.pyplot(fig)

def f(x): 
  return 13*x**2+9*x-12

u = f(t)
fig, ax = plt.subplots(figsize=(16,8))
ax.plot(t, u, label='sin(t)', color='b') 
ax.set_ylabel("")
ax.set_xlabel("t")
ax.tick_params(axis='y', labelsize=20)
ax.set_xticklabels(ax.get_xticklabels(), rotation=30, ha='right')
ax.tick_params(axis='x', labelsize=15)
plt.grid(color='green', linestyle='-.', linewidth=.5)
st.pyplot(fig)

def fungsi(x):
    return 13 * x**2 + 9 * x - 12

def integral_trapesium(x1, x2, n):
    h = (x2 - x1) / n
    integral = 0.5 * (f(x1) + f(x2))

    for i in range(1, n):
        x = x1 + i * h
        integral += fungsi(x)

    return h * integral

fig, ax = plt.subplots(figsize=(16,8))
ax.plot(t, u, label='sin(t)', color='b') 
ax.set_ylabel("")
ax.set_xlabel("t")
ax.tick_params(axis='y', labelsize=20)
ax.set_xticklabels(ax.get_xticklabels(), rotation=30, ha='right')
ax.tick_params(axis='x', labelsize=15)
plt.grid(color='green', linestyle='-.', linewidth=.5)
st.pyplot(fig)
