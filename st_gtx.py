import streamlit as st

st.header("GTX to CSV File Translator")
csv = st.text_input("Enter CSV Data")
if st.button("Convert to GTX..."):
    st.text("GTX of " + csv)

