import pandas as pd
from modules.utils import load_csv, save_csv

FILE = "data/shifts.csv"

def get_data():
    return load_csv(FILE)

def add_shift(new):
    df = get_data()
    df = pd.concat([df, pd.DataFrame([new])], ignore_index=True)
    save_csv(df, FILE)