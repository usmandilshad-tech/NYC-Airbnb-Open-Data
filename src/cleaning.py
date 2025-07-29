import pandas as pd

def load_and_clean_data(file_path):
    df = pd.read_csv(file_path)

    # Drop rows with too many missing values
    df.dropna(subset=['reviews_per_month'], inplace=True)
    df['reviews_per_month'].fillna(0, inplace=True)

    # Convert dates
    df['last_review'] = pd.to_datetime(df['last_review'], errors='coerce')

    # Save cleaned data
    df.to_csv("../output/cleaned_data.csv", index=False)

    return df
