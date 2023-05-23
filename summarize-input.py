import openai

openai.api_key = "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"

input_text = input("Enter text to summarize: ")

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Summarize the following text:"},
        {"role": "user", "content": input_text},
    ],
    temperature=0,
)

ai_response = response.choices[0].message.content
print("Sumarized text:\n\n ", ai_response)
