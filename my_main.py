# my_main.py
# Author: Tristan Riggs

from my_assistant import GymAssistant
from my_tool import GymInfo

MEMBERSHIPS = {"basic": 20, "premium": 40}

gym_tool = GymInfo(MEMBERSHIPS)

bot = GymAssistant("Max", "You are a friendly gym membership assistant.", gym_tool)

print("Type a message, or type quit to stop.")
user_message = input("You: ")

while user_message.lower() != "quit":
    print(f"{bot.name}: {bot.respond(user_message)}")
    user_message = input("You: ")

print(f"Messages in this conversation: {len(bot.history)}")
