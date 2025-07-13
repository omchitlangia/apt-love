# Copyright (c) 2025 Om Chitlangia
# Licensed under the MIT License. See LICENSE file in the project root for full license information.

from install.boot_sequence import boot_sequence
from utils.printer import print_delay
import time, json, os
from utils.swipe_engine import start_swiping
from utils.match_viewer import view_matches
from utils.love_quotes import show_random_quote
from utils.easter_eggs import run_easter_egg
from utils.zodiac import get_zodiac_sign
from utils.truth_dare_engine import truth_or_dare
from utils.mood_scanner import run_mood_scan, run_love_scan, run_nerd_scan, run_ex_scan
from games.date_invaders import start_date_invaders


def install_apt_love():
    print_delay("Reading package lists... Done", 0.03)
    print_delay("Building dependency tree... Done", 0.03)
    print_delay("Reading state information... Done", 0.03)
    print_delay("The following NEW packages will be installed: apt-love", 0.03)
    print_delay("0 upgraded, 1 newly installed, 0 to remove.", 0.03)
    print_delay("Need to get 1.3 MB of emotional archives.", 0.03)
    print_delay("Get:1 https://love.archive.ubuntu.com apt-love.deb [1.3 MB]", 0.03)
    print_delay("Fetched 1.3 MB in 1s (2,400 kB/s)", 0.03)
    print_delay("Setting up apt-love (v1.0) ...", 0.03)
    with open("love_state.json", "w") as f:
        json.dump({"installed": True}, f)

def create_profile():
    INTEREST_OPTIONS = [
        "Compiling from source", "Arch ricing", "ASCII art memes",
        "Reading man pages for fun", "Making Bash scripts that break everything",
        "Emacs vs Vim debates", "Mounting emotional drives",
        "Watching matrix rain in real terminal", "Tor browsing for cat pics",
        "Hacking old CRT monitors", "Writing love letters in Markdown",
        "Running sudo for validation", "Updating system to feel productive",
        "Collecting rare distros", "Arguing on StackOverflow",
    ]
    print_delay("\nWould you like to create a profile now? (Y/n)")
    if input("➤ ").strip().lower() == 'n':
        return

    username = input("👤 Enter your username: ").strip()

    while True:
        age_input = input("🎂 Your age: ").strip()
        if not age_input.isdigit():
            print_delay("🤨 That's not a number.")
            continue
        age = int(age_input)
        if age < 16:
            print_delay("🚫 apt-love is strictly 16+. Come back after some puberty.")
            return
        break

    while True:
        gender = input("🚻 Your gender (male/female): ").strip().lower()
        if gender in ["male", "female"]:
            break
        else:
            print_delay("⚠️  Only male or female. No Apache helicopters.")

    while True:
        preference = input("🚻 Looking for? (male/female/both): ").strip().lower()
        if preference in ["male", "female", "both"]:
            break
        else:
            print_delay("⚠️  Choose from male, female, both.")

    print_delay("\n🌟 Enter your birthday (DD-MM):")
    birthday_input = input("✨ ").strip()
    try:
        day, month = map(int, birthday_input.split("-"))
        zodiac = get_zodiac_sign(day, month)
    except:
        zodiac = "Unknown"
    print_delay(f"✨ Assigned Zodiac Sign: {zodiac}. May your stars be ever in your flavor of bash!")

    print_delay("\n🎯 Choose your top 3 interests:\n")
    for i, item in enumerate(INTEREST_OPTIONS, 1):
        print(f"  [{i}] {item}")

    while True:
        selection = input("\n📅 Enter 3 numbers separated by commas: ").strip()
        if ',' not in selection:
            print_delay("⚠️  Use commas. Like your ex uses mixed signals.")
            continue
        indexes = [int(i.strip()) for i in selection.split(',') if i.strip().isdigit()]
        if len(indexes) != 3 or any(i < 1 or i > len(INTEREST_OPTIONS) for i in indexes):
            print_delay("⚠️  Select exactly 3 valid numbers. It's not a dating buffet.")
        else:
            break

    interests = [INTEREST_OPTIONS[i - 1] for i in indexes]
    fav_cmd = input("💻 Favorite Linux command: ").strip()

    profile = {
        "username": username,
        "age": age,
        "gender": gender,
        "preference": preference,
        "interests": interests,
        "favorite_command": fav_cmd,
        "birthday": birthday_input,
        "zodiac": zodiac
    }

    os.makedirs("data", exist_ok=True)
    with open("data/profile.json", "w") as f:
        json.dump(profile, f, indent=4)
    with open("data/matches.json", "w") as f:
        json.dump([], f)

    print_delay(f"\n✅ Profile created. Welcome, {username}! May your love life be more stable than Arch updates.")

def edit_profile():
    if not os.path.exists("data/profile.json"):
        print_delay("⚠️  No profile to edit.")
        return

    with open("data/profile.json", "r") as f:
        profile = json.load(f)

    print("\n🛠️  What would you like to edit?")
    options = [k for k in profile.keys() if k != "zodiac"]
    for i, key in enumerate(options, 1):
        print(f"  [{i}] {key}")

    print("  [0] Cancel")
    choice = input("➤ ").strip()

    if not choice.isdigit() or int(choice) < 0 or int(choice) > len(options):
        print_delay("❌ Invalid choice.")
        return
    choice = int(choice)

    if choice == 0:
        print_delay("No edits made.")
        return

    key = options[choice - 1]
    new_val = input(f"🔁 New value for {key}: ").strip()

    if key == "interests":
        print_delay("Editing interests. Choose 3 new ones:")
        INTEREST_OPTIONS = [
            "Compiling from source", "Arch ricing", "ASCII art memes",
            "Reading man pages for fun", "Making Bash scripts that break everything",
            "Emacs vs Vim debates", "Mounting emotional drives",
            "Watching matrix rain in real terminal", "Tor browsing for cat pics",
            "Hacking old CRT monitors", "Writing love letters in Markdown",
            "Running sudo for validation", "Updating system to feel productive",
            "Collecting rare distros", "Arguing on StackOverflow",
        ]
        for i, item in enumerate(INTEREST_OPTIONS, 1):
            print(f"  [{i}] {item}")
        while True:
            selection = input("\n📥 Enter 3 numbers separated by commas: ").strip()
            indexes = [int(i.strip()) for i in selection.split(',') if i.strip().isdigit()]
            if len(indexes) != 3:
                print_delay("⚠️  Exactly 3.")
                continue
            profile["interests"] = [INTEREST_OPTIONS[i - 1] for i in indexes]
            break
    elif key == "age":
        if not new_val.isdigit():
            print_delay("⚠️  Numbers only.")
            return
        profile[key] = int(new_val)
    elif key == "birthday":
        profile[key] = new_val
    try:
        day, month = map(int, new_val.split("-"))
        from utils.zodiac import get_zodiac_sign
        profile["zodiac"] = get_zodiac_sign(day, month)
        print_delay(f"🔄 Zodiac updated to: {profile['zodiac']}")
    except:
        print_delay("⚠️ Invalid date. Zodiac not updated.")

    else:
        profile[key] = new_val

    with open("data/profile.json", "w") as f:
        json.dump(profile, f, indent=4)
    print_delay(f"✅ {key} updated.")

def delete_profile():
    if os.path.exists("data/profile.json"):
        os.remove("data/profile.json")
    if os.path.exists("data/matches.json"):
        os.remove("data/matches.json")
    print_delay("🗑️  Profile deleted.")

def uninstall_apt_love():
    if os.path.exists("love_state.json"):
        os.remove("love_state.json")
    delete_profile()
    print_delay("🧹 apt-love uninstalled.")

def main():
    boot_sequence()
    while True:
        cmd = input("root@love-machine:~# ").strip()

        if cmd == "sudo apt install apt-love":
            if os.path.exists("love_state.json"):
                print_delay("Already installed. Chill.")
            else:
                install_apt_love()
                create_profile()
        elif cmd == "create-profile":
            if not os.path.exists("love_state.json"):
                print_delay("⚠️  Install apt-love first.")
            elif os.path.exists("data/profile.json"):
                print_delay("⚠️  You already have a profile.")
            else:
                create_profile()
        elif cmd == "edit-profile":
            edit_profile()
        elif cmd == "delete-profile":
            delete_profile()
        elif cmd == "uninstall apt-love":
            uninstall_apt_love()
        elif cmd == "show-profile":
            if os.path.exists("data/profile.json"):
                with open("data/profile.json") as f:
                    p = json.load(f)
                print("\n👤 Your Profile:")
                for k, v in p.items():
                    if isinstance(v, list):
                        print(f"{k.capitalize()}:")
                        for i in v:
                            print(f"  • {i}")
                    else:
                        print(f"{k.capitalize()}: {v}")
            else:
                print_delay("⚠️  No profile found.")
        elif cmd == "start-dating":
            start_swiping()
        elif cmd == "view-matches":
            view_matches()
        elif cmd == "love-quote":
            show_random_quote()
        elif cmd == "truth-or-dare":
            truth_or_dare()

        elif cmd == "exit":
            print_delay("Logging out but your heart remains logged in... 💔")
            break
        elif cmd.startswith("text "):
            uname = cmd.split(" ",1)[1].strip()
            from utils.chat_engine import start_chat_with
            start_chat_with(uname)
        elif cmd == "mood-scan":
            run_mood_scan()

        elif cmd.startswith("love-scan"):
            parts = cmd.split(" ", 1)
            target = parts[1] if len(parts) > 1 else "your crush"
            run_love_scan(target)

        elif cmd == "nerd-scan":
            run_nerd_scan()

        elif cmd == "ex-scan":
            run_ex_scan()

        elif cmd == "date-invaders":
            start_date_invaders()

        else:
            run_easter_egg(cmd)

if __name__ == "__main__":
    main()
