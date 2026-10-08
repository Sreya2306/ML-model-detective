import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

csv_file_path = "data/sample/pipeline_readings.csv"
df = pd.read_csv(csv_file_path)

# Style
sns.set(style="whitegrid")

# 1. Missing values bar chart
missing_per_column = df.isnull().sum()

plt.figure(figsize=(8, 4))
sns.barplot(x=missing_per_column.index, y=missing_per_column.values)
plt.title("Missing values per column")
plt.xlabel("Column")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("outputs/missing_values_bar.png", dpi=150)
plt.show()

# 2. Histogram of a numeric column
plt.figure(figsize=(6, 4))
sns.histplot(df["inlet_pressure"], bins=5, kde=False)
plt.title("Distribution of inlet pressure")
plt.xlabel("Inlet pressure")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("outputs/inlet_pressure_histogram.png", dpi=150)
plt.show()