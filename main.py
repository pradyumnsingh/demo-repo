import openai

# Replace 'your-api-key' with your actual OpenAI API key
openai.api_key = "your-api-key"

def ask_openai(question):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": question}
            ]
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"An error occurred: {e}"

# Existing code
print("Hello World!")
print("Hello Again")

print(3 + 4)
print(3 * 4)

# Ask GPT-4 a question
question = "What is the capital of France?"
answer = ask_openai(question)
print(f"Question: {question}")
print(f"Answer: {answer}")