import streamlit as st

st.title('Find whether the given number is odd or even.')
a = st.number_input('Enter a number',0)
result = a % 2
if result==0:
  st.write("The Number :",a, ' is Even')
else:
  st.write("The Number :",a, ' is Odd')
