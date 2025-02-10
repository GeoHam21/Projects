import ollama

# Initialize conversation history
conversation_history = []

def chat_with_ai(prompt):
    # Append user input
    conversation_history.append({"role": "user", "content": prompt})

    # Ensure the AI only references actual user messages
    response = ollama.chat(model="llama3", messages=conversation_history)

    # Extract and store AI's response separately
    ai_reply = response["message"]["content"]
    conversation_history.append({"role": "assistant", "content": ai_reply})

    return ai_reply

print("AI: Hello! You can start chatting. Type 'exit' to quit.")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "goodbye"]:
        print("AI: Goodbye!")
        break

    response = chat_with_ai(user_input)
    print("AI:", response)



