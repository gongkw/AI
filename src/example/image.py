from openai import OpenAI
client = OpenAI()

response = client.images.generate(
    prompt="A cute baby sea otter",
    n=2,
    size="1024x1024"
)

print(response.data[0].url)

/*
https://oaidalleapiprodscus.blob.core.windows.net/private/org-taHCvTrOkT2Jc1QrgsTzkPyw/user-FeNGmlHMiezTf8bZ084ZEkwY/img-mFAi3Xp5XC0xqjBeUiR4eRFP.png?st=2024-10-19T04%3A56%3A00Z&se=2024-10-19T06%3A56%3A00Z&sp=r&sv=2024-08-04&sr=b&rscd=inline&rsct=image/png&skoid=d505667d-d6c1-4a0a-bac7-5c84a87759f8&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-10-18T18%3A29%3A45Z&ske=2024-10-19T18%3A29%3A45Z&sks=b&skv=2024-08-04&sig=JECI9HzTfLG%2B5Zpcc9ZIVDuwAsY/Fh66JML2p6ahftc%3D
*/