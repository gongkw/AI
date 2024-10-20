import json

# Define the input and output file names
input_file = 'training_data.jsonl'  # Replace with your actual input file name
output_file = 'trainning_chat_format_data.jsonl'  # Name of the output file

# Read the original data
chat_data = []
with open(input_file, 'r') as json_file:
    for line in json_file:
        if line.strip():  # Skip empty lines
            entry = json.loads(line.strip())
            message_entry = {
                "messages": [
                    {
                        "role": "user",
                        "content": entry["prompt"]
                    },
                    {
                        "role": "assistant",
                        "content": entry["completion"]
                    }
                ]
            }
            chat_data.append(message_entry)
# Save to a new JSON Lines file
with open(output_file, 'w') as json_file:
    for entry in chat_data:
        json_file.write(json.dumps(entry) + '\n')

print(f"Data has been converted and saved to {output_file}.")
