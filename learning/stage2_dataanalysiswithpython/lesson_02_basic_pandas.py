import pandas as pd

csv_file_path="data/sample/pipeline_readings.csv"
df=pd.read_csv(csv_file_path)

print("Dataset shape:",df.shape)
print("Missing values per column:",df.isnull().sum())
print("Duplicate rows:",df.duplicated().sum())
print("Numeric Summaries:",df.describe())