#create a simple agent using if else statements
# Simple AI Agent using if-else statements

print(" Simple AI Agent")
print("Type 'hello', 'weather', 'study', or 'bye'.")

while True:
    user_input = input("You: ").lower()

    if user_input == "hello":
        print("AI: Hello! How can I help you?")

    elif user_input == "weather":
        print("AI: I can't check live weather yet, but I hope it's nice outside!")

    elif user_input == "study":
        print("AI: Great! Let's study Python. Start with variables and if-else statements.")

    elif user_input == "bye":
        print("AI: Goodbye! ")
        break

    else:
        print("AI: Sorry, I don't understand that.")