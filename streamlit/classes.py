import os
import pandas as pd


class Dataset:
    DATABASE_PATH = "datasets"
    def __init__(self, name, df):
        self.name = name
        self.df = df

    @staticmethod
    def add_to_database(df, name):
        file_path = f"{DATABASE_PATH}/{name}.pkl"
        df.to_pickle(file_path)

    @staticmethod
    def list_datasets():
        return os.listdir(Dataset.DATABASE_PATH)

    @staticmethod
    def list_info():
        ...

    @staticmethod
    def load_dataset(name:str):
        df = pd.read_pickle(name)

    @staticmethod
    def remove_dataset():
        ...
