import sys

for line in sys.stdin:
    # Skip the header line
    if line.startswith("Date"):
        continue

    # Strip leading and trailing whitespace
    line = line.strip()

    # Split the line into its components
    date, temperature, _, _, _ = line.split(',')

    # Extract the month (YYYY-MM) from the date
    month = date[:7]

    # Output the key-value pair: month and temperature
    print(f"{month}\t{temperature}")