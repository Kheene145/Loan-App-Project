import pandas as pd
import pickle as pk
import streamlit as st
import sklearn
model = pk.load(open('model.pk1', 'rb'))
scaler = pk.load(open('scaler.pk1', 'rb'))

st.header('Loan Prediction App')

No_of_dependent = st.slider('Choose No of dependant', 0, 5)
grad = st.selectbox('Choose Education', ['Graduated', 'Not Graduated'])
self_emp = st.selectbox('Choose Self_employed ? ', ['Yes', 'No'])
Annual_Income = st.slider('Choose Annual Income', 0, 10000000)
Loan_Amount = st.slider('Choose Loan Amount', 0, 10000000)
Loan_Duration = st.slider('Choose Loan Duration', 0, 20)
Cilbil = st.slider('Choose Cilbil Score', 0, 1000)
Assets = st.slider('Choose Asset', 0, 10000000)

if grad == 'Graduated':
    grad_status = 0
else:
    grad_status = 1


if self_emp == 'No':
    emp_status = 0
else:
    emp_status = 1


if st.button('Predict'):
    pred_data = pd.DataFrame([[No_of_dependent, '1', '0', Annual_Income, Loan_Amount, Loan_Duration, Cilbil,Assets]],
                      columns=['no_of_dependents', 'education', 'self_employed', 'income_annum', 'loan_amount', 'loan_term', 'cibil_score', 'Assets'])

    pred_data = scaler.transform(pred_data)
    predict = model.predict(pred_data)
    if predict[0] == 1:
        st.markdown('Loan is Approved')
    else:
        st.markdown('Loan is Rejected')

