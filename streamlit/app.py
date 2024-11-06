import streamlit as st
import pandas as pd
import functions as f
from classes import Dataset
    
st.set_page_config(layout="wide")
st.subheader("""Analiza i projektowanie obiektowe""")

data_tab, analysis_tab, visual_tab, auto_tab = st.tabs(["Dane", "Analiza", "Wizualizacja", "Automatyzacja"])

with data_tab:
    data = st.file_uploader("Upload new dataset", type=["csv", 'xlsx'])
    if data:
        st.write("Data preview:")
        df = pd.read_csv(data)
        st.dataframe(df)
        default_name = str(data.name).split(".")[0]
        name = st.text_input("Dataset name", value=data.name)
        add_button=st.button("add to databse")
        if add_button:
            if f.validate_name(name):
                Dataset.add_to_database(df, name)
            else:
                 st.warning("Dataset already exists")

        st.subheader("Available datasets")
        datasets_name = Dataset.list_datasets()
        for name in datasets_name:
            st.write(f"[name]")
        st.write()

with analysis_tab:
    datasets_name = Dataset.list_datasets()
    