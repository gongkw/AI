from openai import OpenAI
client = OpenAI()

# Set up OpenAI API key , export OPENAI_API_KEY="your_api_key_here"

# Initialize the conversation thread
thread =[{"role": "system", "content": "You are a professional assistant."}]

# Function to add user message to thread and run the assistant
def run_thread(user_input):
    # Add user message
    thread.append({"role": "user", "content": user_input})
    
    # Run the thread by asking the assistant for a response
    response = client.chat.completions.create(
        model="gpt-4o", 
        messages=thread
     
    ) 
    # Extract assistant's response and add it to the thread
    assistant_message = response.choices[0].message.content
    thread.append({"role": "assistant", "content": assistant_message})
    
    return assistant_message

# Simulate a conversation
while True:
    # Get user input
    user_input = input("You: ")
    
    # Break loop if user wants to stop
    if user_input.lower() in ['exit', 'quit']:
        break
    
    # Get assistant response and display it
    assistant_response = run_thread(user_input)
    print(f"Assistant: {assistant_response}")
