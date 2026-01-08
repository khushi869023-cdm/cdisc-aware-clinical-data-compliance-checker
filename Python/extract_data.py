import pandas as pd

# Step 1: Load raw clinical trial data
df = pd.read_csv("../data/raw/clinical_trial_data.csv")


# Step 2: Display basic info
print("Dataset shape (rows, columns):", df.shape)
print("\nColumn names:")
print(df.columns)

# Step 3: Save processed copy
df.to_csv("../data/processed/clinical_trial_processed.csv", index=False)

print("\nData extraction completed successfully.")
