import streamlit as st
from modules.leave import get_data, apply_leave

def show():
    st.title("Leave Management")

    df = get_data()
    st.dataframe(df)

    st.subheader("Apply Leave")

    emp = st.text_input("Employee ID")
    l_type = st.selectbox("Leave Type", ["Annual", "Sick", "Paternity", "Maternity", "Loss of Pay"])
    start = st.date_input("Start Date")
    end = st.date_input("End Date")

    if st.button("Apply"):
        # Capture the success status
        success = apply_leave({
            "emp_id": emp,
            "leave_type": l_type,
            "start_date": str(start),
            "end_date": str(end),
            "status": "Pending"
        })

        if success:
            st.success("Leave applied successfully!")
            st.rerun()
        else:
            st.error("Duplicate entry: A leave request already exists for this employee starting on this date.")