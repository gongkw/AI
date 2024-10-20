import json
import openai
import csv

# Set your OpenAI API key

# Load the JSONL test data
test_data = []
with open("Evaluation_AAPL_data.jsonl", "r") as file:  # Replace with actual file path
    for line in file:
        test_data.append(json.loads(line))

# Function to generate prediction from the fine-tuned model
def generate_prediction(volatility, transaction_factor):
    user_input = f"Volatility: {volatility}, Transaction Factor: {transaction_factor}"
    
    # Send the prompt to the fine-tuned model
    completion = openai.chat.completions.create(
        model="ft:gpt-4o-mini-2024-07-18:personal::AKJCwTZg",  # Replace with your fine-tuned model ID
        messages=[
            {"role": "system", "content": "You are a stock price prediction assistant."},
            {"role": "user", "content": user_input}
        ]
    )
    
    print(completion.choices[0].message)


    # Extract the predicted completion (stock price)
    predicted_stock_price = float(completion.choices[0].message.content.strip().split(":")[-1])
    print (predicted_stock_price)
    return predicted_stock_price

# Store predictions and comparison results
predictions = []
comparison_results = []

# Iterate through test data, generate predictions and compare
for entry in test_data:
    volatility = float(entry["prompt"].split(",")[0].split(":")[-1].strip())
    transaction_factor = float(entry["prompt"].split(",")[1].split(":")[-1].strip())
    actual_stock_price = float(entry["completion"].split(":")[-1].strip())
    
    print (volatility, transaction_factor, actual_stock_price)
    # Generate prediction
    predicted_stock_price = generate_prediction(volatility, transaction_factor)
    
    # Compare signs (if both positive or both negative, prediction is correct)
    if (predicted_stock_price >= 0 and actual_stock_price >= 0) or (predicted_stock_price < 0 and actual_stock_price < 0):
        comparison_result = 1  # Correct prediction
    else:
        comparison_result = 0  # Incorrect prediction
    
    # Store predictions
    predictions.append({
        "volatility": volatility,
        "transaction_factor": transaction_factor,
        "actual_stock_price": actual_stock_price,
        "predicted_stock_price": predicted_stock_price,
        "correct": comparison_result
    })

# Write predictions to CSV file
csv_file_path = "predictions_results.csv"  # Specify your CSV file path

# Define CSV header
csv_columns = ["volatility", "transaction_factor", "actual_stock_price", "predicted_stock_price", "correct"]

try:
    with open(csv_file_path, mode='w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=csv_columns)      
        writer.writeheader()
        for prediction in predictions:
            writer.writerow(prediction)
    print(f"Predictions successfully written to {csv_file_path}")
except IOError:
    print("I/O error occurred while writing to the CSV file")
