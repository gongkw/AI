import csv

# Load the predictions from the CSV file
csv_file_path = "predictions_results.csv"  # Replace with your file path

true_positive = 0
false_positive = 0
true_negative = 0
false_negative = 0

# Read the CSV file
with open(csv_file_path, mode='r') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        actual_stock_price = float(row["actual_stock_price"])
        predicted_stock_price = float(row["predicted_stock_price"])
        correct = int(row["correct"])
        
        if correct == 1:
            if predicted_stock_price >= 0:
                true_positive += 1  # Correct positive prediction
            else:
                true_negative += 1  # Correct negative prediction
        else:
            if predicted_stock_price >= 0:
                false_positive += 1  # Incorrect positive prediction
            else:
                false_negative += 1  # Incorrect negative prediction

# Calculate metrics
total_predictions = true_positive + true_negative + false_positive + false_negative

accuracy = (true_positive + true_negative) / total_predictions if total_predictions else 0
precision = true_positive / (true_positive + false_positive) if (true_positive + false_positive) else 0
recall = true_positive / (true_positive + false_negative) if (true_positive + false_negative) else 0

# Output the results
print(f"Accuracy: {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
