import streamlit as st
from modules.attendance import get_data, add_record

def show():
    st.title("Attendance")

    df = get_data()
    st.dataframe(df)

    st.subheader("Add Attendance")

    emp = st.text_input("Employee ID")
    date = st.date_input("Date")
    status = st.selectbox("Status", ["Present", "Absent", "Leave"])

    if st.button("Submit"):
        success = add_record({
            "emp_id": emp,
            "date": str(date),
            "status": status
        })

        if success:
            st.success("Added")
        else:
            st.error("Duplicate entry")