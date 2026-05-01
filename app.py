import streamlit as st
from modules.auth import USERS
from modules.sidebar import render_sidebar

st.set_page_config(page_title="HR SaaS Dashboard", layout="wide")

def load_css():
    with open("assets/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
load_css()

# LOGIN
if "user" not in st.session_state:
    st.markdown('<div class="title">HR Management System</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Modern workforce management platform</div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        username = st.text_input("Username", value="admin")
        password = st.text_input("Password", type="password", value="admin123")
        if st.button("Login"):
            if username in USERS and USERS[username]["password"] == password:
                st.session_state["user"] = username
                st.session_state["role"] = USERS[username]["role"]
                st.rerun()
            else:
                st.error("Invalid credentials")
        st.markdown("---")
        if st.button("Quick Admin Login"):
            st.session_state["user"] = "admin"
            st.session_state["role"] = "admin"
            st.rerun()
    st.stop()

# SIDEBAR
page = render_sidebar()

# HEADER
col1, col2 = st.columns([6, 2])
with col1:
    st.markdown('<div class="title"></div>', unsafe_allow_html=True)
with col2:
    st.markdown(f'<div class="user-badge">{st.session_state["user"]}</div>', unsafe_allow_html=True)
    if st.button("Logout"):
        st.session_state.clear()
        st.rerun()
st.markdown("---")

# ROUTING — inline imports instead of st.switch_page
if page == "Dashboard":
    from pages.dashboard import show
    show()
elif page == "Attendance":
    from pages.attendance import show
    show()
elif page == "Leave":
    from pages.leave import show
    show()
elif page == "Shifts":
    from pages.shifts import show
    show()