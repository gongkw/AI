import json
import openai


# Load the JSONL test data
test_data = []
with open("Evaluation_AAPL_data.jsonl", "r") as file:  # Replace with actual file path
    for line in file:
        test_data.append(json.loads(line))

# Preview the first entry of the test data (optional)
print(test_data[0])


