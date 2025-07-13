import json
import random
import os
from utils.printer import print_delay
from utils.ascii_art import show_match_animation
from utils.zodiac import signs_are_compatible

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
    print(f"💻 Username: {profile['username']}")
    print(f"🎂 Age: {profile['age']}")
    print(f"🚻 Gender: {profile.get('gender', 'N/A')}")
    print(f"🔮 Zodiac Sign: {profile.get('zodiac', 'Unknown')}")
    print("🎯 Interests:")
    for interest in profile['interests']:
        print(f"   • {interest}")
    print(f"💻 Fav Command: {profile['favorite_command']}")
    print("=" * 40)

def calculate_match(user, candidate):
    shared = set(user["interests"]) & set(candidate["interests"])
    count = len(shared)

    user_sign = user.get("zodiac", "Unknown")
    candidate_sign = candidate.get("zodiac", "Unknown")
    zodiac_bonus = signs_are_compatible(user_sign, candidate_sign) if user_sign != "Unknown" and candidate_sign != "Unknown" else False

    # Interest-based logic + zodiac boost
    if count >= 2:
        return True
    elif count == 1:
        return random.random() < (0.4 + 0.2 if zodiac_bonus else 0.4)
    else:
        return random.random() < (0.1 + 0.2 if zodiac_bonus else 0.1)

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
    pref = user.get("preference", "both")
    if pref != "both":
        pool = [p for p in pool if p.get("gender") == pref]

    random.shuffle(pool)
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
                user_sign = user.get("zodiac", "Unknown")
                candidate_sign = candidate.get("zodiac", "Unknown")

                if user_sign != "Unknown" and candidate_sign != "Unknown":
                    if signs_are_compatible(user_sign, candidate_sign):
                        print_delay(f"🔮 Cosmic Approval: {user_sign} ❤️ {candidate_sign} — stars are aligned!")
                    else:
                        print_delay(f"🌩️ Uh-oh: {user_sign} & {candidate_sign} are astrologically allergic... but hey, opposites attract?")

                show_match_animation()
                save_match(candidate)
            else:
                print_delay("😢 No spark... even Mercury is in retrograde.")
        else:
            print("❓ Invalid choice. Skipping...")

        shown += 1

    print_delay("\n📁 Session ended. Type start-dating to continue swiping.")
