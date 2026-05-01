import pandas as pd
import os
from modules.utils import load_csv, save_csv

FILE = "data/leaves.csv"
COLUMNS = ["emp_id", "leave_type", "start_date", "end_date", "status"]

def get_data():
    if not os.path.exists(FILE):
        return pd.DataFrame(columns=COLUMNS)
    df = load_csv(FILE)
    return df if (df is not None and not df.empty) else pd.DataFrame(columns=COLUMNS)

def apply_leave(new):
    df = get_data()

    # Duplicate check: Same employee, same start date
    if not df.empty:
        exists = ((df['emp_id'] == new['emp_id']) & 
                  (df['start_date'] == new['start_date'])).any()
        if exists:
            return False

    new_row = pd.DataFrame([new])
    df = pd.concat([df, new_row], ignore_index=True)
    save_csv(df, FILE)
    return True