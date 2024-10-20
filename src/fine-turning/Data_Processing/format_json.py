import csv
import json

# Define input and output file paths
csv_file_path = 'Evaluation_AAPL_data.csv'  # Your CSV file path
jsonl_file_path = 'Evaluation_AAPL_data.jsonl'  # Output JSONL file

# Open CSV and JSONL files
with open(csv_file_path, 'r') as csv_file, open(jsonl_file_path, 'w') as jsonl_file:
    csv_reader = csv.DictReader(csv_file)

    # Loop through rows in CSV and format them as prompt/completion pairs
    for row in csv_reader:
        prompt = (
            f"Volatility: {row['Volatility']}, "
            f"Transaction Factor: {row['Daily_Volume_transaction']}"
        )
        completion = f"Stock Price: {row['Daily_Return']}"
        
        # Create JSON object for each row
        json_obj = {
            "prompt": prompt,
            "completion": completion
        }
        
        # Write JSON object to file
        jsonl_file.write(json.dumps(json_obj) + '\n')
