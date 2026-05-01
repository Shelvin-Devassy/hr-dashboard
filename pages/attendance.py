import streamlit as st
from modules.attendance import get_data, add_record
from datetime import time

def show():
    st.title("Attendance")

    df = get_data()
    st.dataframe(df)

    st.subheader("Add Attendance")

    emp = st.text_input("Employee ID")
    date = st.date_input("Date")
    in_time = st.time_input("Check In Time", time(9, 0))
    out_time = st.time_input("Check Out Time", time(17, 0))
    status = st.selectbox("Status", ["Present", "Absent", "Leave"])

    if st.button("Submit"):
        val_in = str(in_time.strftime("%H:%M")) if status == "Present" else ""
        val_out = str(out_time.strftime("%H:%M")) if status == "Present" else ""
        success = add_record({
            "emp_id": emp,
            "date": str(date),
            "check_in": val_in,
            "check_out": val_out,
            "status": status
        })

        if success:
            st.success("Added")
            st.rerun()
        else:
            st.error("Record already exists.")