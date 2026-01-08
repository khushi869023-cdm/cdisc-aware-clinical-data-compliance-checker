import pandas as pd

# Load processed data
df = pd.read_csv("../data/processed/clinical_trial_processed.csv")

# Define key fields that should not be missing
key_fields = [
    "NCT Number",
    "Title",
    "Status",
    "Conditions",
    "Interventions",
    "Study Type"
]

# Count missing key fields per record
df["Missing_Key_Fields"] = df[key_fields].isnull().sum(axis=1)

# Flag problematic records
df["Data_Issue_Flag"] = df["Missing_Key_Fields"].apply(
    lambda x: "Yes" if x > 0 else "No"
)

# Summary
issue_summary = df["Data_Issue_Flag"].value_counts()

print("\n--- Record-level Data Issues ---")
print(issue_summary)

# Save flagged records
df.to_csv("../data/processed/record_level_issues.csv", index=False)

print("\nRecord-level completeness check completed.")

