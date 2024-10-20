from openai import OpenAI
client = OpenAI()

client.files.create(
  file=open("trainning_chat_format_data.jsonl", "rb"),
  purpose="fine-tune"
)


