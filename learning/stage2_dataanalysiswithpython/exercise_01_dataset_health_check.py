import pandas as pd

csv_file_path="data/sample/pipeline_readings.csv"
df=pd.read_csv(csv_file_path)

print("Number of rows and columns:",df.shape)
print("Column names:",df.columns.tolist())
print("Datatypes:",df.dtypes)
print("Missing values per columns",df.isnull().sum())
print("Duplicate rows:",df.duplicated())
print("Numeric Summaries:",df.describe())
if df.isnull().sum().sum() >10: print("WARNING:data is missing")
if df.duplicated().sum()>0:print("WARNING:Duplicate data is found")