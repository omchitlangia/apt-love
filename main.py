from install.boot_sequence import boot_sequence
from utils.printer import print_delay
import time, json, os

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
    print_delay("✅ apt-love installed successfully.\n", 0.03)
    with open("love_state.json", "w") as f:
        json.dump({"installed": True}, f)

def create_profile():
    print_delay("\nWould you like to create a profile now? (Y/n)")
    choice = input("➤ ").lower()
    if choice == 'n':
        return
    print_delay("Let's set up your profile.\n")
    username = input("Enter your username: ")
    age = input("Enter your age: ")
    interests = input("Your interests (comma-separated): ")
    fav_cmd = input("Your favorite Linux command: ")
    profile = {
        "username": username,
        "age": age,
        "interests": [x.strip() for x in interests.split(',')],
        "favorite_command": fav_cmd
    }
    os.makedirs("data", exist_ok=True)
    with open("data/profile.json", "w") as f:
        json.dump(profile, f, indent=4)
    print_delay(f"\n✅ Profile created successfully, {username}!")

def main():
    boot_sequence()
    while True:
        cmd = input("root@love-machine:~# ").strip()
        if cmd == "sudo apt install apt-love":
            install_apt_love()
            create_profile()
            break
        elif cmd == "exit":
            print("Logging out...")
            break
        else:
            print(f"bash: {cmd}: command not found")

if __name__ == "__main__":
    main()
