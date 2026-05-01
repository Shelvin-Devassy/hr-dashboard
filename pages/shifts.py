import streamlit as st
from modules.schedule import get_data, add_shift
import datetime
import time

def show():
    st.title("Shift Scheduling")

    df = get_data()
    st.dataframe(df)

    st.subheader("Assign Shift")

    emp = st.text_input("Employee ID")
    date = st.date_input("Date")
    shift = st.selectbox("Shift", ["Morning", "Evening"])
    start = st.time_input("Start Time", datetime.time(9, 0))
    end = st.time_input("End Time", datetime.time(17, 0))

    if st.button("Assign"):
        # Capture the boolean result from the module
        success = add_shift({
            "emp_id": emp,
            "date": str(date),
            "shift": shift,
            "start_time": start.strftime("%H:%M"),
            "end_time": end.strftime("%H:%M")
        })

        if success:
            st.success("Shift assigned successfully!")
            time.sleep(2)
            st.rerun()
        else:
            st.error("Duplicate entry: This employee already has a shift on this date.")