
import streamlit as st
from streamlit import sidebar

st.title('Loan Calculator')
st.write('kindly enter your details')
a=st.radio('Are you a Government employee',options=['Yes','No'])
if a=='Yes':
    st.write('you will have reduced interest rates')
else:
    st.write('ok')
b=st.checkbox('are you looking for loan')
if b==1:
    st.write('welcome to the eligibility interface')

st.sidebar.title('Policies')
st.sidebar.write("1. lorem\n2. ipsum\n3. dolor\n")
st.sidebar.button('accept')


def eligible():
    if y > 50000:
        if x < 700:
            output_placeholder.write('Not eligible')
        else:
            output_placeholder.write('Eligible for the loan')
    else:
        output_placeholder.write('Not eligible due to low salary')

st.button('submit',on_click=eligible)