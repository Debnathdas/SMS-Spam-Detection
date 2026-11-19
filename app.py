
import streamlit as st
import pandas as pd
from src.predict import predict_sms

st.set_page_config(
    page_title="SMS Spam Detection",
    page_icon="📩",
    layout="centered"
)

if "history" not in st.session_state:
    st.session_state.history = []

st.title("📩 SMS Spam Detection")
st.write("Detect spam messages using Machine Learning.")

message = st.text_area(
    "Enter your SMS message",
    placeholder="Type your SMS here..."
)

if st.button("Analyze Message", type="primary"):

    try:
        result = predict_sms(message)

        if result == "SPAM":
            st.error("🚨 Spam message detected!")
        else:
            st.success("✅ This is a legitimate message.")

        st.session_state.history.append({
            "Message": message,
            "Prediction": result
        })

    except ValueError as error:
        st.warning(str(error))

st.divider()

st.subheader("Prediction History")

if st.session_state.history:
    st.dataframe(
        pd.DataFrame(st.session_state.history),
        use_container_width=True
    )

    if st.button("Clear History"):
        st.session_state.history = []
        st.rerun()
else:
    st.info("No prediction history available.")
