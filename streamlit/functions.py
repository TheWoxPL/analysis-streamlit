# Funkcje 
import pandas as pd
from classes import Dataset

def validate_name(name):
    existing_names = [
        name.replace(".pkl", ".")
    ]
    if name in Dataset.list_datasets():
        return false

DATABASE_PATH="datasets"

def add_to_database(df, name):
    file_path = f"{DATABASE_PATH}/{name}.pkl"
    df.to_pickle(file_path)
