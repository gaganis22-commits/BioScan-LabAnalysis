import pandas as pd
import os

# Optional: Print current working directory (for debugging in Jenkins)
print("Current working directory:", os.getcwd())

# Example data for analysis
data = {
    'SampleID': [101, 102, 103, 104],
    'Measurement': [23.5, 19.8, 25.1, 22.0],
    'Status': ['Pass', 'Fail', 'Pass', 'Pass']
}

# Create DataFrame
df = pd.DataFrame(data)

# Save CSV in current directory (workspace)
output_file = "results.csv"
df.to_csv(output_file, index=False)

print(f"CSV file '{output_file}' created successfully!")
