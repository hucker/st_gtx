import streamlit as st

st.header("GTX to CSV File Translator")
csv = st.text("Enter CS")
if st.button("Convert to GTX..."):
    st.text("GTX of " + csv)

