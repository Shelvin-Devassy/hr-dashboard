import streamlit as st
from modules.schedule import get_data, add_shift

def show():
    st.title("Shift Scheduling")

    df = get_data()
    st.dataframe(df)

    emp = st.text_input("Employee ID")
    date = st.date_input("Date")
    shift = st.selectbox("Shift", ["Morning", "Evening"])

    if st.button("Assign"):
        add_shift({
            "emp_id": emp,
            "date": str(date),
            "shift": shift
        })
        st.success("Shift assigned")