# Operational Anomaly Detector (Python)
This project is a lightweight decision-support tool for detecting unusual operational events in CSV files.
It automatically analyzes numeric metrics (e.g. cost, duration, volume) and highlights anomalies using statistical deviation analysis.

## Problem
Operational and finance teams often work with large CSV exports.
Manually identifying unusual values is time-consuming and error-prone.

## Solution
The script:
- Loads any CSV file
- Automatically detects numeric columns
- Identifies anomalies using Z-score analysis
- Explains *why* a value is considered anomalous
- Outputs a clean anomaly report

## Technology
- Python
- Pandas
- NumPy
- Google Colab compatible

## Example Use Cases
- Operational performance monitoring
- Cost anomaly detection
- Delivery time analysis
- Transaction volume validation

## Output
The result is a CSV file containing:
- row index
- metric name
- value
- anomaly score
- classification (MEDIUM / HIGH)
- human-readable explanation

## Disclaimer
This tool provides decision support only.
Final business decisions should always involve human validation.
