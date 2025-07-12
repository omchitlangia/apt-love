import json
import random
import time
from utils.printer import print_delay
from utils.chat_engine_ai import ai_reply  # ← uses TinyLLaMA

def get_personality():
    return random.choice(["nerd", "romantic", "chaotic", "dry"])

def start_chat_with(username):
    try:
        with open("data/matches.json") as f:
            matches = json.load(f)
    except FileNotFoundError:
        print_delay("⚠️  No matches found.")
        return

    matched = next((m for m in matches if m["username"] == username), None)
    if not matched:
        print_delay(f"❌ No match found with username: {username}")
        return

    personality = get_personality()
    print_delay(f"\n📱 Chatting with {username} (personality: {personality})")
    print_delay("Type your message. Type 'exit' to return.\n")

    while True:
        user_msg = input("you 💬: ").strip()
        if user_msg.lower() == "exit":
            print_delay("💻 Exiting chat...\n")
            break

        # Simulate "typing..." animation
        print(f"{username} 💚 is typing...", end="\r")
        time.sleep(1 + len(user_msg) * 0.05)

        # Get reply
        reply = ai_reply(user_msg, personality, matched["interests"])

        # Clear the line
        print(" " * 60, end="\r")

        # Show actual reply with typing effect
        print_delay(f"{username} 💚: {reply}")
