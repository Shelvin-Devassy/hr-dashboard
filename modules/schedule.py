import pandas as pd
import os
from modules.utils import load_csv, save_csv

FILE = "data/shifts.csv"
COLUMNS = ["emp_id", "date", "shift", "start_time", "end_time"]

def get_data():
    if not os.path.exists(FILE):
        return pd.DataFrame(columns=COLUMNS)
    df = load_csv(FILE)
    return df if (df is not None and not df.empty) else pd.DataFrame(columns=COLUMNS)

def add_shift(new):
    df = get_data()

    # Check for duplicate: Same employee, same date
    if not df.empty:
        exists = ((df['emp_id'] == new['emp_id']) & (df['date'] == new['date'])).any()
        if exists:
            return False # Indicate failure

    new_row = pd.DataFrame([new])
    df = pd.concat([df, new_row], ignore_index=True)
    save_csv(df, FILE)
    return True # Indicate success