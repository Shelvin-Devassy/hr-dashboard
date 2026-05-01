import streamlit as st
from modules.leave import get_data, apply_leave

def show():
    st.title("Leave Management")

    df = get_data()
    st.dataframe(df)

    st.subheader("Apply Leave")

    emp = st.text_input("Employee ID")
    start = st.date_input("Start Date")
    end = st.date_input("End Date")

    if st.button("Apply"):
        apply_leave({
            "emp_id": emp,
            "start_date": str(start),
            "end_date": str(end),
            "status": "Pending"
        })
        st.success("Leave applied")