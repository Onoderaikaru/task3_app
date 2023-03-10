import streamlit as st
from scipy.optimize import minimize

def my_function(x):
    return x[0]**2 + x[1]**2

st.title("My Optimization App")

x0 = st.number_input("x0:", value=0)
x1 = st.number_input("x1:", value=0)

res = minimize(my_function, [x0, x1])

st.write("Optimization results:")
st.write("x0: ", res.x[0])
st.write("x1: ", res.x[1])
st.write("Function value: ", res.fun)
