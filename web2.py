import streamlit as st
import numpy as np
import plotly.express as pe
st.title("Welcome to rising stars")
st.subheader("power")
st.checkbox("testing")
x=st.number_input("Enter a number",value=0,format="%d")
y=st.number_input("Enter Exponent",value=0,format="%d")
if st.button("press here"):
    result=x**y
    st.write(f"{x} power {y} is {result}")
st.title("plotting graph")
x=st.number_input("Enter starting range",value=0,format="%d")
y=st.number_input("Enter last range",value=0,format="%d")
z=st.number_input("Enter power",value=0,format="%d")
if st.button("Graph"):
    x1=np.linspace(x,y,100)
    y1=[i**z for i in x1]
    fig=pe.line(x=x1,y=y1)
    st.plotly_chart(fig)



    
