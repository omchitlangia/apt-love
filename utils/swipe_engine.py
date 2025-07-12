import json
import random
import os
from utils.printer import print_delay
from utils.ascii_art import show_match_animation

MATCH_FILE = "data/matches.json"

def load_user_profile():
    if not os.path.exists("data/profile.json"):
        print_delay("⚠️ No user profile found.")
        return None
    with open("data/profile.json") as f:
        return json.load(f)

def load_match_pool():
    with open("data/match_pool.json") as f:
        return json.load(f)

def show_ascii_card(profile):
    print("\n" + "=" * 40)
    print(f"💻  Username: {profile['username']}")
    print(f"🎂  Age: {profile['age']}")
    print("🎯  Interests:")
    for interest in profile['interests']:
        print(f"   • {interest}")
    print(f"💻  Fav Command: {profile['favorite_command']}")
    print("=" * 40)

def calculate_match(user, candidate):
    shared = set(user["interests"]) & set(candidate["interests"])
    count = len(shared)
    if count >= 2:
        return True
    elif count == 1:
        return random.random() < 0.4
    else:
        return random.random() < 0.1

def save_match(profile):
    os.makedirs("data", exist_ok=True)
    if os.path.exists(MATCH_FILE):
        with open(MATCH_FILE, "r") as f:
            matches = json.load(f)
    else:
        matches = []

    matches.append(profile)
    with open(MATCH_FILE, "w") as f:
        json.dump(matches, f, indent=4)

def start_swiping():
    user = load_user_profile()
    if not user:
        return

    pool = load_match_pool()
    random.shuffle(pool)  # Shuffle for randomness
    shown = 0

    for candidate in pool:
        if shown >= 5:
            break
        show_ascii_card(candidate)
        print("💘 Swipe [l = like, r = skip, q = quit]")
        choice = input("➤ ").strip().lower()

        if choice == "q":
            break
        elif choice == "r":
            print_delay("❌ Skipped.")
        elif choice == "l":
            if calculate_match(user, candidate):
                show_match_animation()
                save_match(candidate)

            else:
                print_delay("😢 No spark... maybe next one.")
        else:
            print("❓ Invalid choice. Skipping...")

        shown += 1

    print_delay("\n📁 Session ended. Run again to swipe more.")
