from install.boot_sequence import boot_sequence
from utils.printer import print_delay
import time, json, os, shutil

def install_apt_love():
    print_delay("Reading package lists... Done", 0.03)
    print_delay("Building dependency tree... Done", 0.03)
    print_delay("Reading state information... Done", 0.03)
    print_delay("The following NEW packages will be installed: apt-love", 0.03)
    print_delay("0 upgraded, 1 newly installed, 0 to remove.", 0.03)
    print_delay("Need to get 1.3 MB of archives.", 0.03)
    print_delay("Get:1 https://love.archive.ubuntu.com apt-love.deb [1.3 MB]", 0.03)
    print_delay("Fetched 1.3 MB in 1s (2,400 kB/s)", 0.03)
    print_delay("Selecting previously unselected package apt-love.", 0.03)
    print_delay("Preparing to unpack apt-love.deb ...", 0.03)
    print_delay("Unpacking apt-love (v1.0) ...", 0.03)
    print_delay("Setting up apt-love (v1.0) ...", 0.03)
    print_delay("Processing triggers for man-db (2.10.2-1) ...", 0.03)
    print_delay("✅ apt-love installed successfully.\n", 0.03)
    with open("love_state.json", "w") as f:
        json.dump({"installed": True}, f)

def create_profile():
    INTEREST_OPTIONS = [
        "Compiling from source",
        "Arch ricing",
        "ASCII art memes",
        "Reading man pages for fun",
        "Making Bash scripts that break everything",
        "Emacs vs Vim debates",
        "Mounting emotional drives",
        "Watching matrix rain in real terminal",
        "Tor browsing for cat pics",
        "Hacking old CRT monitors",
        "Writing love letters in Markdown",
        "Running sudo for validation",
        "Updating system to feel productive",
        "Collecting rare distros",
        "Arguing on StackOverflow",
    ]

    print_delay("\nWould you like to create a profile now? (Y/n)")
    choice = input("➤ ").strip().lower()
    if choice == 'n':
        return

    print_delay("\nLet's set up your profile.")
    username = input("\n👤 Enter your username: ").strip()
    while True:
        age_input = input("🎂 Your age: ").strip()
        if not age_input.isdigit():
            print_delay("🤨 That's not a number. Try again.")
            continue
        age = int(age_input)
        if age < 16:
            print_delay("🚫 Sorry kiddo, apt-love is strictly 16+.")
            print_delay("Go touch some grass, and try again in a few years 🌱🧃.")
            return
        break



    print_delay("\n🎯 Choose your top 3 interests from the list below:\n")
    for i, item in enumerate(INTEREST_OPTIONS, 1):
        print(f"  [{i}] {item}")

    print_delay("\n📥 Enter exactly 3 numbers separated by commas (e.g. 1,5,12):")

    selected_indexes = []
    while True:
        selection = input("➤ ").strip()
        if ',' not in selection:
            print_delay("⚠️  Use commas to separate your choices (e.g. 2,4,9). Try again.")
            continue
        selected_indexes = [int(i.strip()) for i in selection.split(',') if i.strip().isdigit()]
        if len(selected_indexes) != 3 or any(i < 1 or i > len(INTEREST_OPTIONS) for i in selected_indexes):
            print_delay("⚠️  Please enter exactly 3 valid numbers from the list (e.g. 1,5,12).")
        else:
            break

    interests = [INTEREST_OPTIONS[i - 1] for i in selected_indexes]

    fav_cmd = input("💻 Your favorite Linux command: ").strip()

    profile = {
        "username": username,
        "age": age,
        "interests": interests,
        "favorite_command": fav_cmd
    }

    os.makedirs("data", exist_ok=True)
    with open("data/profile.json", "w") as f:
        json.dump(profile, f, indent=4)

    print_delay(f"\n✅ Profile created successfully, {username}!")


def uninstall_apt_love():
    removed = False
    if os.path.exists("love_state.json"):
        os.remove("love_state.json")
        removed = True
    if os.path.exists("data/profile.json"):
        os.remove("data/profile.json")
        removed = True
    if os.path.exists("data") and not os.listdir("data"):
        os.rmdir("data")
    print_delay("🧹 apt-love uninstalled." if removed else "apt-love is not installed.")

def delete_profile():
    if os.path.exists("data/profile.json"):
        os.remove("data/profile.json")
        print_delay("🗑️  Profile deleted successfully.")
        if os.path.exists("data") and not os.listdir("data"):
            os.rmdir("data")
    else:
        print_delay("⚠️  No profile found.")

def main():
    boot_sequence()
    while True:
        cmd = input("root@love-machine:~# ").strip()
        if cmd == "sudo apt install apt-love":
            if os.path.exists("love_state.json"):
                print_delay("apt-love is already installed.")
            else:
                install_apt_love()
                create_profile()
        elif cmd == "uninstall apt-love":
            uninstall_apt_love()
        elif cmd == "show-profile":
            if not os.path.exists("data/profile.json"):
                print_delay("⚠️  No profile found. Use create-profile to make one.")
            else:
                with open("data/profile.json", "r") as f:
                    profile = json.load(f)
                print_delay("\n📄 Your Profile:")
                print(f"👤 Username: {profile.get('username')}")
                print(f"🎂 Age: {profile.get('age')}")
                print("🎯 Interests:")
                for interest in profile.get("interests", []):
                    print(f"   - {interest}")
                print(f"💻 Favorite command: {profile.get('favorite_command')}")
                print()

        elif cmd == "edit-profile":
            if not os.path.exists("data/profile.json"):
                print_delay("⚠️  No profile found to edit. Use create-profile first.")
            else:
                print_delay("\n🛠️ Let's edit your profile.\n")
                os.remove("data/profile.json")
                create_profile()

        elif cmd == "create-profile":
            if not os.path.exists("love_state.json"):
                print_delay("⚠️  apt-love is not installed. Run: sudo apt install apt-love")
            elif os.path.exists("data/profile.json"):
                print_delay("⚠️  A profile already exists. Use delete-profile first if you want to remake it.")
            else:
                create_profile()
        elif cmd == "delete-profile":
            delete_profile()
        elif cmd == "exit":
            print_delay("Logging out...\n")
            break
        else:
            print(f"bash: {cmd}: command not found")

if __name__ == "__main__":
    main()
