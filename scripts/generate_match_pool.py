import json
import random
import os
from utils.zodiac import get_zodiac_sign  # Make sure zodiac.py is in utils/

INTEREST_OPTIONS = [
    "Compiling from source", "Arch ricing", "ASCII art memes",
    "Reading man pages for fun", "Making Bash scripts that break everything",
    "Emacs vs Vim debates", "Mounting emotional drives",
    "Watching matrix rain in real terminal", "Tor browsing for cat pics",
    "Hacking old CRT monitors", "Writing love letters in Markdown",
    "Running sudo for validation", "Updating system to feel productive",
    "Collecting rare distros", "Arguing on StackOverflow"
]

FEMALE_NAMES = [
    "packet_princess", "cli_queen", "root_doll", "manpage_bae", "neovim_nymph",
    "sudo_sweetheart", "markdown_mermaid", "dev_damsel", "bashful_babe", "r00tgrl",
    "matrix_mistress", "hackette", "distro_diva", "arch_angel", "catnip_coder"
]

MALE_NAMES = [
    "vim_king", "bash_beast", "kernel_crush", "ascii_dude", "emacs_warrior",
    "sudo_bro", "cli_chad", "manpager", "rootzilla", "g33k_lord",
    "packet_sniffer", "stackoverlord", "cmdline_lover", "neovim_knight", "distromancer"
]

FAV_COMMANDS = [
    "sudo rm -rf /", "ls -lAh", "chmod +x love.sh", "htop", "neofetch", "man man", "curl -I google.com",
    "echo $HOME", "nmap -sV", "alias love='cat /dev/soul'"
]

def generate_fake_birthday():
    day = random.randint(1, 28)
    month = random.randint(1, 12)
    return f"{day:02d}-{month:02d}", day, month

def generate_profiles():
    profiles = []

    for name in FEMALE_NAMES:
        birthday_str, day, month = generate_fake_birthday()
        profile = {
            "username": name,
            "gender": "female",
            "age": str(random.randint(19, 27)),
            "birthday": birthday_str,
            "zodiac": get_zodiac_sign(day, month),
            "interests": random.sample(INTEREST_OPTIONS, 3),
            "favorite_command": random.choice(FAV_COMMANDS)
        }
        profiles.append(profile)

    for name in MALE_NAMES:
        birthday_str, day, month = generate_fake_birthday()
        profile = {
            "username": name,
            "gender": "male",
            "age": str(random.randint(19, 27)),
            "birthday": birthday_str,
            "zodiac": get_zodiac_sign(day, month),
            "interests": random.sample(INTEREST_OPTIONS, 3),
            "favorite_command": random.choice(FAV_COMMANDS)
        }
        profiles.append(profile)

    os.makedirs("data", exist_ok=True)
    with open("data/match_pool.json", "w") as f:
        json.dump(profiles, f, indent=4)

    print("✅ Generated 30 fake profiles in data/match_pool.json")

if __name__ == "__main__":
    generate_profiles()
