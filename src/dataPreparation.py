import glob
import pandas as pd

def load_dataframes(path_class="data/raw/"):
    return pd.concat(map(pd.read_csv, glob.glob(f'{path_class}*.csv')))


def sort_dataframe_by_date(df):
    df['created_at'] = pd.to_datetime(df['created_at'])
    df.sort_values(by=['created_at'], inplace=True)
    df.reset_index(drop=True, inplace=True)
    return df

def drop_columns(df):
    columns_to_drop = ['id_str', 'truncated', 'lang', 'retweeted', 'favorited', 'geo', 'coordinates',
                       'contributors', 'metadata', 'source', 'in_reply_to_status_id',
                       'in_reply_to_status_id_str', 'in_reply_to_user_id', 'in_reply_to_user_id_str',
                       'in_reply_to_screen_name', 'place', 'is_quote_status', 'retweet_count',
                       'favorite_count', 'extended_entities', 'quoted_status_id', 'quoted_status_id_str',
                       'quoted_status']
    df = df.drop(columns=columns_to_drop)
    return df

def drop_duplicates(df):
    df.drop_duplicates(keep=False, inplace=True)
    return df

def normalize_entities(df):
    df2 = pd.json_normalize(df['entities'].apply(str).apply(eval))
    df = pd.concat([df, df2], axis=1)
    df = df.drop(columns='entities')
    return df

def drop_user_column(df):
    df = df.drop(columns='user')
    return df

def save_dataframe_to_csv(df, path, title):
    """
    Saves a DataFrame to a CSV file.

    Args:
        df: The DataFrame to save.
        path (str): The path to the directory where the CSV file will be saved.
        title (str): The title or name of the CSV file.

    Returns:
        None
    """
    file_path = f'{path}{title}.csv'
    df.to_csv(file_path, index=False)
    print(f"DataFrame saved to: {file_path}")



