import streamlit as st
import ten8t

st.header(f"GTX to CSV File Translator (ten8t-{ten8t.__version__)} ")
csv = st.text_input("Enter CSV Data")
if st.button("Convert to GTX..."):
    st.text("GTX of " + csv)

uploaded_file = st.file_uploader("Choose CSV file with GTX ata")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)
