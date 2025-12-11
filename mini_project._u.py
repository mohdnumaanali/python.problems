import random

name = input("What is your name: ").strip().title()
print(f"Good morning, {name}! ☀️")
print(f"How are you, {name}?")

good_replies = [
    "That's awesome to hear!",
    "Glad to know you're doing great!",
    "Nice! Keep that positive energy up!",
    "Wow, that's wonderful!"
]

normal_replies = [
    "Ohh, okay! Hope your day gets better 😊",
    "Fine is still good — stay positive!",
    "Average days make great ones feel special, right?"
]

bad_replies = [
    "Oh no, I hope things get better soon 😢",
    "Stay strong, better days are coming!",
    "Don’t worry, everything will be okay."
]
reply = input("Reply: ").lower().strip()

if any(word in reply for word in ["good", "great", "nice", "excellent", "happy"]):
    print(random.choice(good_replies))
elif any(word in reply for word in ["normal", "fine", "average", "okay"]):
    print(random.choice(normal_replies))
else:
    print(random.choice(bad_replies))

reply2 = input("Where are you from: ").lower().strip()

if "warangal" in reply2:
    print("Ohh! You're from my city — nice to meet you! 🏙️")
elif "hyderabad" in reply2:
    print("You’re from my state! I love Hyderabad 😍")
else:
    print(f"{reply2.title()} sounds like a beautiful place! I’d love to visit one day 🌍")

closing_lines = [
    "It was nice chatting with you!",
    "Thanks for the chat 😊 Have a great day!",
    "Take care and keep smiling 😄",
    "Bye! Hope to talk again soon 👋"
]

print(random.choice(closing_lines))

question = print("hey if your free we can play a game : ")

reply3 = input(" reply : ")

if reply3 == "yes" :
    print(" oh that's nice ")
else: 
    print("oh then we can play next time ")
