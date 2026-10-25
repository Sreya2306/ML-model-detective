from data_checks import (
    load_dataset,
    get_dataset_shape,
    get_column_names,
    get_missing_values,
    get_duplicate_count,
    get_numeric_summary,
    check_missing_values,
    check_duplicates,
    check_class_balance,
)

csv_file_path = "data/sample/pipeline_readings.csv"
target_column = "leak_detected"

df = load_dataset(csv_file_path)

print("ML Model Detective — Dataset Health Check")
print("=" * 40)

print("Rows and columns:", get_dataset_shape(df))
print("Column names:", get_column_names(df))
print("\nMissing values per column:")
print(get_missing_values(df))
print("\nDuplicate rows:", get_duplicate_count(df))
print("\nNumeric summary:")
print(get_numeric_summary(df))

print("\nWarnings:")
warnings = check_missing_values(df) + check_duplicates(df)

if warnings:
    for warning in warnings:
        print("-", warning)
else:
    print("- No data-quality warnings found.")

print("\nWarnings:")

warnings = (
    check_missing_values(df)
    + check_duplicates(df)
    + check_class_balance(df, target_column)
)

if warnings:
    for warning in warnings:
        print("-", warning)
else:
    print("- No data-quality warnings found.")