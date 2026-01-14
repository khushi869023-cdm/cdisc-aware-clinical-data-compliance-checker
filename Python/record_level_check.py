# Phase 1: Structural and reliability checks to determine if the dataset
# is safe to use for downstream clinical validation

import pandas as pd
# Load processed clinical data
df = pd.read_csv("../clinical_trial_processed.csv")

# Define critical CDM fields
critical_fields = [
    "NCT Number",
    "Title",
    "Status",
    "Conditions",
    "Study Type"
]

# Count missing critical fields per record
df["Missing_Critical_Fields"] = df[critical_fields].isnull().sum(axis=1)

# Flag records with issues
df["Record_Issue_Flag"] = df["Missing_Critical_Fields"].apply(
    lambda x: "Query Required" if x > 0 else "OK"
)

# Summary for CDM review
summary = df["Record_Issue_Flag"].value_counts()

print("\n--- Record Level Data Quality Summary ---")
print(summary)

# Save detailed file
df.to_csv("../data/processed/record_level_quality.csv", index=False)

print("\nRecord-level data quality check completed.")


