import streamlit as st

# simple hardcoded users
USERS = {
    "admin": {"password": "admin123", "role": "admin"},
    "emp1": {"password": "123", "role": "employee"}
}

def login():
    st.sidebar.title("Login")

    # username = st.sidebar.text_input("Username")
    username = st.sidebar.text_input(
        "Username",
        value="admin"
    )
    # password = st.sidebar.text_input("Password", type="password")
    password = st.sidebar.text_input(
        "Password",
        type="password",
        value="admin123"
    )

    if st.sidebar.button("Login"):
        if username in USERS and USERS[username]["password"] == password:
            st.session_state["user"] = username
            st.session_state["role"] = USERS[username]["role"]
            st.success("Logged in")
        else:
            st.error("Invalid credentials")

def check_auth():
    return "user" in st.session_state