import pandas as pd


def load_dataset(file_path):
    return pd.read_csv(file_path)


def get_dataset_shape(df):
    return df.shape


def get_column_names(df):
    return df.columns.tolist()


def get_missing_values(df):
    return df.isnull().sum()


def get_duplicate_count(df):
    return df.duplicated().sum()


def get_numeric_summary(df):
    return df.describe()


def check_missing_values(df, warning_threshold=10):
    missing = df.isnull().sum()
    warnings = []

    for column, missing_count in missing.items():
        if missing_count > warning_threshold:
            warnings.append(
                f"Column '{column}' has {missing_count} missing values."
            )

    return warnings


def check_duplicates(df):
    duplicate_count = df.duplicated().sum()

    if duplicate_count > 0:
        return [f"Dataset contains {duplicate_count} duplicate rows."]

    return []