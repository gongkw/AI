from openai import OpenAI
client = OpenAI()

thread_message = client.beta.threads.messages.create(
  "thread_Ul9XPmPZuoZpzNM2hxChXTmD",
  role="user",
  content="How does AI work? Explain it in simple terms.",
)
print(thread_message)


Message(id='msg_TPj4VtldRVem8gkeLh9oh7Ad', assistant_id=None, attachments=[], completed_at=None, content=[TextContentBlock(text=Text(annotations=[], value='How does AI work? Explain it in simple terms.'), type='text')], created_at=1729321616, incomplete_at=None, incomplete_details=None, metadata={}, object='thread.message', role='user', run_id=None, status=None, thread_id='thread_Ul9XPmPZuoZpzNM2hxChXTmD')