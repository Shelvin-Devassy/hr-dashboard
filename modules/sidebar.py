import streamlit as st

def render_sidebar():
    st.sidebar.title("HR")
    page = st.sidebar.radio(
        "",  # empty label
        ["Dashboard", "Attendance", "Leave", "Shifts"],
        label_visibility="collapsed"
    )
    return page