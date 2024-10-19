from openai import OpenAI
client = OpenAI()

empty_thread = client.beta.threads.create()
print(empty_thread)