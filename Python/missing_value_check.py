import pandas as pd

# Load processed clinical data
df = pd.read_csv("../data/processed/clinical_trial_processed.csv")

print("\n--- Missing Value Summary ---")

# Count missing values per column
missing_counts = df.isnull().sum()

# Calculate missing percentage
missing_percent = (missing_counts / len(df)) * 100

# Combine into one table
missing_summary = pd.DataFrame({
    "Missing_Count": missing_counts,
    "Missing_Percent": missing_percent.round(2)
})

print(missing_summary)

# Save report for dashboard / review
missing_summary.to_csv("../data/processed/missing_value_report.csv")

print("\nMissing value check completed.")
