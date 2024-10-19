from openai import OpenAI
client = OpenAI()

response = client.beta.assistants.delete("xxxxxx")
print(response)
