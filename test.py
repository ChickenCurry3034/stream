import streamlit as st
import pandas as pd
import numpy as np
import pickle
select=st.sidebar.selectbox('Choode the dataset',('Iris', 'USA_Housing', 'Cancer'))

with open('iris_brain','rb') as file:
    pred=pickle.load(file)

if select == 'Iris':
    st.title('Iris Flower Prediction Model by Aarush')
    a=st.number_input('Enter Sepal Length')
    b=st.number_input('Enter Sepal Width')
    c=st.number_input('Enter Petal Length')
    d=st.number_input('Enter Petal Width')
    rst=pred.predict([[a,b,c,d]])
    st.write("The given value belongs to",rst[0])
elif select=='USA_Housing':
    st.title('USA Housing Prediction Model by Aarush')
    a=st.number_input('a')
    b=st.number_input('b')
    c=st.number_input('c')
    d=st.number_input('d')
elif select=='Cancer':
    st.title('Cancer Prediction Model by Aarush')
    a=st.number_input('a')
    b=st.number_input('b')
    c=st.number_input('c')
    d=st.number_input('d')
