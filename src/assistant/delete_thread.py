from openai import OpenAI
client = OpenAI()

response = client.beta.threads.delete("xxxxxx")
print(response)
