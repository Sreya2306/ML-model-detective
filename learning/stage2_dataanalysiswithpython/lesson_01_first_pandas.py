import pandas as pd

csv_file_path="data/sample/pipeline_readings.csv"
df=pd.read_csv(csv_file_path)

print("Dataset Shape(rows,columns):",df.shape)
print("First few rows:",df.head())
print("Column names:",df.columns.tolist())
print("Datatypes:",df.dtypes)
