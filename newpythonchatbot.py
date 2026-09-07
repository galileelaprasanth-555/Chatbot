import ollama

def get_ai_response(user_text):
    response = ollama.chat(
        model="llama3.2:latest",
        messages=[
            {
                "role": "user",
                "content": user_text
            }
        ]
    )

    return response["message"]["content"]


print("AI Chatbot started! Type 'exit' to stop.")

while True:
    user_text = input("You: ")

    if user_text.lower() == "exit":
        print("Goodbye!")
        break

    answer = get_ai_response(user_text)
    print("NANI AI:", answer)