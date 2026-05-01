import streamlit as st
import pandas as pd
import plotly.express as px
from modules.attendance import get_data
from modules.utils import load_csv

def show():
    st.title("Advanced HR Analytics")

    df = get_data()

    if df.empty:
        st.warning("No data available")
        st.stop()

    emp_df = load_csv("data/employees.csv")

    # merge attendance with employee data
    if not emp_df.empty:
        df = df.merge(emp_df, on="emp_id", how="left")

    # =========================
    # DATA PREP
    # =========================
    df["date"] = pd.to_datetime(df["date"])

    # =========================
    # FILTERS
    # =========================
    col1, col2 = st.columns(2)

    with col1:
        start_date = st.date_input("Start Date", df["date"].min())

    with col2:
        end_date = st.date_input("End Date", df["date"].max())

    df = df[(df["date"] >= pd.to_datetime(start_date)) &
            (df["date"] <= pd.to_datetime(end_date))]

    # =========================
    # KPI METRICS
    # =========================
    total = len(df)
    present = len(df[df["status"] == "Present"])
    leave = len(df[df["status"] == "Leave"])

    attendance_rate = round((present / total) * 100, 2) if total > 0 else 0

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Records", total)
    col2.metric("Present", present)
    col3.metric("On Leave", leave)
    col4.metric("Attendance %", f"{attendance_rate}%")

    st.markdown("---")
    #-------------------------------
    # st.markdown("Department-wise Attendance")

    if "department" in df.columns:
        fig_dept = px.bar(
            df,
            x="department",
            color="status",
            title="Department Performance"
        )
        st.plotly_chart(fig_dept, use_container_width=True)

    # =========================
    # ATTENDANCE TREND
    # =========================
    trend = df.groupby("date")["status"].count().reset_index()

    fig_trend = px.line(
        trend,
        x="date",
        y="status",
        title="Attendance Trend Over Time",
        markers=True
    )

    st.plotly_chart(fig_trend, use_container_width=True)

    # =========================
    # STATUS DISTRIBUTION
    # =========================
    fig_pie = px.pie(
        df,
        names="status",
        title="Attendance Distribution"
    )

    st.plotly_chart(fig_pie, use_container_width=True)

    #-----------------------------------
    st.markdown("Weekly Attendance Pattern")

    df["day"] = df["date"].dt.day_name()

    heat = df.pivot_table(
        index="day",
        columns="status",
        aggfunc="size",
        fill_value=0
    )

    st.dataframe(heat)

    # =========================
    # LEAVE ANALYSIS
    # =========================
    leave_df = df[df["status"] == "Leave"]

    if not leave_df.empty:
        leave_trend = leave_df.groupby("date").size().reset_index(name="count")

        fig_leave = px.bar(
            leave_trend,
            x="date",
            y="count",
            title="Leave Trend"
        )

        st.plotly_chart(fig_leave, use_container_width=True)

    # =========================
    # SMART INSIGHTS
    # =========================
    st.markdown("Insights")

    if attendance_rate > 90:
        st.success("Excellent attendance rate!")
    elif attendance_rate > 75:
        st.info("Good attendance, but can improve.")
    else:
        st.warning("Attendance is low. Needs attention.")

    # Top leave day
    if not leave_df.empty:
        top_day = leave_df["date"].value_counts().idxmax()
        st.write(f"Highest leave recorded on: **{top_day.date()}**")