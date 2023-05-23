import openai

openai.api_key = ""

input_text = ""

with open("text.txt", "r") as file:
    input_text = file.read()

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Você é uma ferramenta de criação de ementas de acórdãos de Tribunais. Seu papel é ler o acórdão e criar uma ementa para ele."},
        {"role": "user", "content": input_text},
    ],
    temperature=0,
)

ai_response = response.choices[0].message.content
print("Sumarized text:\n\n ", ai_response)

with open("summary.txt", "w") as file:
    file.write(ai_response)
