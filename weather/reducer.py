import sys

current_month = None
temp_sum = 0.0
temp_count = 0

for line in sys.stdin:
    # Strip leading and trailing whitespace
    line = line.strip()

    # Parse the input we got from the mapper
    month, temperature = line.split('\t')

    # Convert temperature to float
    temperature = float(temperature)

    # If switching to a new month, output the average temperature of the previous month
    if current_month == month:
        temp_sum += temperature
        temp_count += 1
    else:
        if current_month:
            # Calculate the average temperature
            avg_temp = temp_sum / temp_count
            print(f"{current_month}\t{avg_temp:.2f}")
        
        current_month = month
        temp_sum = temperature
        temp_count = 1

# Don't forget to output the last month's average temperature
if current_month == month:
    avg_temp = temp_sum / temp_count
    print(f"{current_month}\t{avg_temp:.2f}")