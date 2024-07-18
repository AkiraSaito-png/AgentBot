import openai


openai.api_key = ''

def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # Você pode substituir pelo modelo desejado
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    user_prompt = "Tell me a joke about AI."
    gpt_response = chat_with_gpt(user_prompt)
    print(f"ChatGPT: {gpt_response}")

