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
        # Typing animation with dots
        typing_time = min(3.5, 1.5 + len(user_msg) * 0.07)  # max 3.5 seconds
        start = time.time()
        dot_count = 0

        while time.time() - start < typing_time:
            dots = "." * (dot_count % 4)
            print(f"{username} 💚 is typing{dots}{' ' * (3 - len(dots))}", end="\r")
            dot_count += 1
            time.sleep(0.4)

        # Clear the line after typing
        print(" " * 60, end="\r")


        # Get reply
        reply = ai_reply(user_msg, personality, matched["interests"])

        # Clear the line
        print(" " * 60, end="\r")

        # Show actual reply with typing effect
        print_delay(f"{username} 💚: {reply}")
