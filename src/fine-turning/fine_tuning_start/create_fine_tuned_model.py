from openai import OpenAI
client = OpenAI()

client.fine_tuning.jobs.create(
  training_file="file-vyNRAQTxZRgAsa52mt33Kj93",
  model="gpt-4o-mini-2024-07-18"
)