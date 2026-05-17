import datetime

def chatbot(user_input):
    user_input = user_input.lower().strip()

    if user_input in ["hello", "hi", "hey"]:
        return "Hi there! I am PyBot. How can I help you today?"

    elif user_input == "how are you":
        return "I am just a bot, but I am running perfectly!"

    elif user_input == "what is your name":
        return "My name is PyBot — your friendly Python chatbot!"

    elif user_input == "what time is it":
        now = datetime.datetime.now().strftime("%H:%M")
        return f"The current time is {now}."

    elif user_input == "tell me a joke":
        return "Why do programmers prefer dark mode? Light attracts bugs!"

    elif user_input in ["bye", "goodbye", "exit", "quit"]:
        return "Goodbye! Have a wonderful day! See you next time."

    else:
        return "Hmm, I did not understand that. Try saying hello!"


print("PyBot is ready! Type bye to exit.")
print("-" * 35)

while True:
    user_msg = input("You: ")
    reply = chatbot(user_msg)
    print("PyBot:", reply)
    if user_msg.lower().strip() in ["bye", "goodbye", "exit", "quit"]:
        break
