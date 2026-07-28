import ollama

print("Welcome to NasirAI!")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    try:
        response = ollama.chat(
            model="llama3.2:latest",
            messages=[
                {"role": "user", "content": user_input}
            ]
        )

        print("\nNasirAI:", response["message"]["content"])
        print()

    except Exception as e:
        print("Error:", e)