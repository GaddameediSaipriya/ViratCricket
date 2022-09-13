%%writefile app.py
import streamlit as st
import joblib
model = joblib.load('virat')
st.title('Virat Centuries')
ip = st.text_input('Enter the out/Notout')
op = model.predict([ip])
if st.button('predict'):
  st.title(op[0])
  
  
  
  
  
