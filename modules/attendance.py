import pandas as pd
from modules.utils import load_csv, save_csv

FILE = "data/attendance.csv"

def get_data():
    return load_csv(FILE)

def add_record(new):
    df = get_data()

    required_cols = ['emp_id', 'date', 'status']
    for col in required_cols:
        if col not in df.columns:
            pass

    # prevent duplicate entry
    exists = ((df['emp_id'] == new['emp_id']) & (df['date'] == new['date'])).any()

    if exists:
        return False

    df = pd.concat([df, pd.DataFrame([new])], ignore_index=True)
    save_csv(df, FILE)
    return True