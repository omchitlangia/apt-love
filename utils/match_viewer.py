import json
import os
from utils.printer import print_delay

def view_matches():
    path = "data/matches.json"
    if not os.path.exists(path):
        print_delay("📭 No matches found yet!")
        return

    with open(path, "r") as f:
        matches = json.load(f)

    if not matches:
        print_delay("📭 No matches found yet!")
        return

    print_delay("\n💖 YOUR MATCHES 💖\n")
    for match in matches:
        print("=" * 40)
        print(f"💻  Username: {match['username']}")
        print(f"🎂  Age: {match['age']}")
        print("🎯  Interests:")
        for interest in match['interests']:
            print(f"   • {interest}")
        print(f"🎂 Birthday: {match['birthday']}")
        print(f"🔮 Zodiac Sign: {match['zodiac']}")
        print(f"💻  Fav Command: {match['favorite_command']}")
        print("=" * 40)
