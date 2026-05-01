import pandas as pd
import random
import os

# =========================
# CONFIG
# =========================

employees = [
    "E001","E002","E003","E004","E005",
    "E006","E007","E008","E009","E010"
]

start_date = "2026-01-01"
end_date = "2026-04-30"

# Shift definitions
SHIFTS = {
    "Morning": ("09:00", "17:00"),
    "Evening": ("13:00", "21:00")
}

# =========================
# SETUP
# =========================

os.makedirs("data", exist_ok=True)

dates = pd.date_range(start=start_date, end=end_date)

attendance_data = []
shift_data = []

# =========================
# GENERATE DATA
# =========================

for emp in employees:

    # Assign fixed shift per employee (realistic)
    emp_shift = random.choice(list(SHIFTS.keys()))
    start_time, end_time = SHIFTS[emp_shift]

    for date in dates:

        # Skip weekends
        if date.weekday() >= 5:
            continue

        # Status distribution (realistic)
        status = random.choices(
            ["Present", "Absent", "Leave"],
            weights=[88, 8, 4]
        )[0]

        # -------------------------
        # Attendance Logic
        # -------------------------
        if status == "Present":

            # Late logic (some days)
            is_late = random.choice([False, False, True])

            if is_late:
                check_in = f"{start_time[:2]}:{random.randint(15,45):02d}"
            else:
                check_in = f"{start_time[:2]}:{random.randint(0,15):02d}"

            check_out = f"{end_time[:2]}:{random.randint(0,30):02d}"

        else:
            check_in = ""
            check_out = ""

        attendance_data.append({
            "emp_id": emp,
            "date": date.strftime("%Y-%m-%d"),
            "check_in": check_in,
            "check_out": check_out,
            "status": status
        })

        # -------------------------
        # Shift Logic
        # -------------------------
        shift_data.append({
            "emp_id": emp,
            "date": date.strftime("%Y-%m-%d"),
            "shift": emp_shift,
            "start_time": start_time,
            "end_time": end_time
        })

# =========================
# CREATE DATAFRAMES
# =========================

attendance_df = pd.DataFrame(attendance_data)
shift_df = pd.DataFrame(shift_data)

# =========================
# SAVE FILES
# =========================

attendance_df.to_csv("data/attendance.csv", index=False)
shift_df.to_csv("data/shifts.csv", index=False)

# =========================
# OUTPUT
# =========================

print("Files generated successfully!")
print(f"attendance.csv rows: {len(attendance_df)}")
print(f"shifts.csv rows: {len(shift_df)}")