import ollama

def chat_with_ai(prompt):
    response = ollama.chat(model="mistral", messages=[{"role": "user", "content": prompt}])
    return response["message"]["content"]

while True:
    user_input = input("You:")
    if user_input.lower() in ["exit", "quit", "goodbye"]:
        print("Goodbye!")
        break

    response = chat_with_ai(user_input)
    print("AI:", response)