import streamlit as st
import pandas as pd
import joblib

model = joblib.load("fraud_detection_pipeline.pkl")

st.title("Aplicación para detección de fraude")

st.markdown("Por favor, ingresa los detalles de la trasnacción y pulsa el botón de predecir")

st.divider()

transaction_type = st.selectbox("Tipo de transacción", ["PAYMENT", "TRANSFER", "CASH_OUT", "DEPOSIT"])
amount = st.number_input("Monto", min_value = 0.0, value = 1000.0)
oldbalanceOrg = st.number_input("Saldo inicial de la cuenta (destinatario)", min_value = 0.0, value = 10000.0)
newbalanceOrig = st.number_input("Nuevo saldo de la cuenta (Destinatario)", min_value = 0.0, value = 9000.0)
oldbalanceDest = st.number_input("Aniguo saldo  de la cuenta (receptor)", min_value = 0.0, value = 0.0)
newbalanceDest = st.number_input("Nuevo saldo de la cuenta (recepor)", min_value = 0.0, value = 0.0)

if st.button("Predecir"):
    input_data = pd.DataFrame([{
        "type" : transaction_type,
        "Amount" : amount,
        "oldbalanceOrg" : oldbalanceOrg,
        "newbalanceOrig" : newbalanceOrig,
        "oldbalanceDest" : oldbalanceDest,
        "newbalanceDest" : newbalanceDest
    }])


    prediction = model.predict(input_data)[0]

    st.subheader(f"predicción : '{int(prediction)}'")

    if prediction == 1:
        st.error("Esta transacción puede ser fraudulenta")
    
    else:
        st.success("Genial! la transacción se encuentra fuera de riesgo")