import re
import pandas as pd

# Step 1: Parse Apache log file
def parse_log(file_path):
    pattern = re.compile(r'(?P<ip>\d+\.\d+\.\d+\.\d+).*\[(?P<timestamp>.*?)\] "(?P<request>.*?)" (?P<status>\d{3})')
    entries = []

    with open(file_path, 'r') as f:
        for line in f:
            match = pattern.match(line)
            if match:
                entries.append(match.groupdict())

    return pd.DataFrame(entries)

# Step 2: Detect Brute Force Attacks (many 401/403 from same IP)
def detect_brute_force(df):
    brute_df = df[df['status'].isin(['401', '403'])]
    return brute_df['ip'].value_counts()[brute_df['ip'].value_counts() > 2]

# Step 3: Detect Directory Traversal Attempts
def detect_traversal(df):
    return df[df['request'].str.contains(r'\.\./', regex=True)]

# Step 4: Detect High Request Spikes (Top 5 IPs by frequency)
def detect_request_spike(df):
    return df['ip'].value_counts().head(5)

# Main
if __name__ == "__main__":
    df = parse_log("sample_logs/access.log")

    print("\n=== Parsed Log Preview ===")
    print(df.head())

    print("\n=== Brute Force IPs (>=3 suspicious attempts) ===")
    print(detect_brute_force(df))

    print("\n=== Directory Traversal Attempts ===")
    print(detect_traversal(df))

    print("\n=== Top 5 IPs by Request Count ===")
    print(detect_request_spike(df))
