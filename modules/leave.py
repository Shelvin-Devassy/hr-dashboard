import pandas as pd
from modules.utils import load_csv, save_csv

FILE = "data/leaves.csv"

def get_data():
    return load_csv(FILE)

def apply_leave(new):
    df = get_data()
    df = pd.concat([df, pd.DataFrame([new])], ignore_index=True)
    save_csv(df, FILE)