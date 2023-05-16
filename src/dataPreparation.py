import glob
import pandas as pd

def load_dataframes(path_class="data/raw/"):
    return pd.concat(map(pd.read_csv, glob.glob(f'{path_class}*.csv')))