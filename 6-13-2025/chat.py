import json
import random
talk = input("Enter the topic: ").lower()

with open('chat.json') as f:
    data = json.load(f)

if talk == "hi":
    print("Greetings:", random.choice(data["greetings"]))
elif talk in data["Info"][0]:
    print("Info:", data["Info"][0][talk])
else:
    print("Sorry, I don’t understand that topic.")