import pandas as pd
import numpy as np
from google.colab import files
import os

# STEP 1 — Upload file

uploaded = files.upload()
file_name = list(uploaded.keys())[0]

os.makedirs("results", exist_ok=True)
print(f"Processing file: {file_name}")

# STEP 2 — Load data

df = pd.read_csv(file_name)

numeric_cols = df.select_dtypes(include=np.number).columns.tolist()

if len(numeric_cols) == 0:
    raise ValueError("No numeric columns found. Cannot perform anomaly detection.")

# STEP 3 — Anomaly detection

results = []

for col in numeric_cols:
    mean = df[col].mean()
    std = df[col].std()

    for idx, value in enumerate(df[col]):
        z_score = abs((value - mean) / std) if std != 0 else 0

        if z_score >= 3:
            decision = "HIGH ANOMALY"
            reason = f"{col} significantly outside normal range"
        elif z_score >= 2:
            decision = "MEDIUM ANOMALY"
            reason = f"{col} moderately outside normal range"
        else:
            decision = "NORMAL"
            reason = "Within expected range"

        results.append({
            "row_index": idx,
            "metric": col,
            "value": round(value, 2),
            "z_score": round(z_score, 2),
            "classification": decision,
            "reason": reason
        })

# STEP 4 — Results

result_df = pd.DataFrame(results)
result_df = result_df[result_df["classification"] != "NORMAL"]

output_path = "results/anomaly_report.csv"
result_df.to_csv(output_path, index=False)

print("Anomaly detection completed.")
print(f"Report saved to {output_path}")

result_df.head(10)
