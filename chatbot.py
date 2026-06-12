import random
from datetime import datetime

print("=" * 50)
print("🤖 Smart AI Chatbot")
print("Type 'help' for commands")
print("Type 'bye' to exit")
print("=" * 50)

jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Python is my favorite snake.",
    "There are 10 types of people: those who understand binary and those who don't."
]

while True:
    user = input("\nYou: ").lower().strip()

    if user == "hello":
        print("Bot: Hello! Nice to meet you.")

    elif user == "how are you":
        print("Bot: I'm doing great. Thanks for asking!")

    elif user == "time":
        current_time = datetime.now().strftime("%H:%M:%S")
        print("Bot: Current time is", current_time)

    elif user == "date":
        current_date = datetime.now().strftime("%d-%m-%Y")
        print("Bot: Today's date is", current_date)

    elif user == "joke":
        print("Bot:", random.choice(jokes))

    elif user == "python":
        print("Bot: Python is a powerful programming language.")

    elif user == "help":
        print("""
Available Commands:
hello
how are you
time
date
joke
python
help
bye
""")

    elif user == "bye":
        print("Bot: Goodbye! Have a great day.")
        break

    else:
<<<<<<< HEAD
        print("Bot: Sorry, I don't understand that command.")
=======
        print("Bot: Sorry, I don't understand that command.")
>>>>>>> 4f52e86c8e6f050ca1341a0d68a82fbd4686dfcc
