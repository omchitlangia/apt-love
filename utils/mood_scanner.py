import random
import time
from utils.printer import print_delay
import json
import os

# Base moods
MOOD_DIAGNOSES = [
    "Clingy but cacheable 💾",
    "Ghosting tendencies detected 👻",
    "Romantically overclocked 💓⚙️",
    "Stable... but only on Ubuntu 14.04 🐧",
    "Emotionally sandboxed 🏖️",
    "Optimistic but prone to segmentation faults 💥",
    "Buffer overflow of feelings 🫠",
    "Dual-booting between hope and despair 💔💾",
    "Sweet, but uses tabs instead of spaces 😬",
    "Flaky like an Arch update 🌧️",
    "Snappy but secretly flatpacked 😈",
]

NERD_COMMENTS = [
    "You alias 'ls' to 'exa'. Respect.",
    "You've used sed in a romantic confession.",
    "You dual-boot Arch and BSD just for fun.",
    "You own a ThinkPad with stickers of editors.",
    "You rewrote your rice 12 times last week.",
    "You installed Gentoo on your toaster.",
]

EX_COMMENTS = [
    "Still emotionally piped to your last breakup.",
    "You're over them... except for the playlist.",
    "Residual love.conf detected in /etc.",
    "Heart.log shows occasional system errors.",
    "You’ve uninstalled them… but forgot to clear cache.",
]

LOVE_COMMENTS = [
    "You're the rsync to their scp — a perfect sync.",
    "They’d run your script without reading it first. That’s love.",
    "Together you’re like Vim and :wq — never truly leaving.",
    "They see your raw Linux energy. It's hot.",
    "They completed your sudo apt-get install <3",
]

def run_mood_scan():
    print_delay("🧠 Analyzing keyboard pressure...")
    time.sleep(0.6)
    print_delay("⌨️ Measuring typing velocity...")
    time.sleep(0.5)
    print_delay("📉 Detecting sarcasm levels...")
    time.sleep(0.5)
    print_delay("💾 Accessing cached feelings...")
    time.sleep(0.6)
    mood = random.choice(MOOD_DIAGNOSES)
    print_delay(f"\n🧠 Mood detected: {mood}")

def run_nerd_scan():
    print_delay("🔍 Scanning your ~/.bash_history...")
    time.sleep(0.5)
    print_delay("📦 Counting sudo usage...")
    time.sleep(0.5)
    print_delay("⚙️ Checking obscure programming language loyalty...")
    time.sleep(0.5)
    nerd = random.choice(NERD_COMMENTS)
    level = random.randint(65, 99)
    print_delay(f"\n💡 Nerd Level: {level}%")
    print_delay(f"🧠 {nerd}")

def run_ex_scan():
    print_delay("💔 Searching terminal memory for emotional residue...")
    time.sleep(0.5)
    print_delay("🪦 Locating deleted playlists...")
    time.sleep(0.5)
    print_delay("🗑️ Analyzing love.log for traces...")
    time.sleep(0.5)
    result = random.choice(EX_COMMENTS)
    temp = random.randint(-5, 10)
    print_delay(f"\n🧊 Emotional temperature: {temp}°C")
    print_delay(f"😐 {result}")

def run_love_scan(target_name="them"):
    print_delay(f"💘 Scanning romantic compatibility with: {target_name}...")
    time.sleep(0.6)
    print_delay("🔍 Parsing emotional metadata...")
    time.sleep(0.6)
    print_delay("📈 Hashing shared trauma...")
    time.sleep(0.5)
    love = random.choice(LOVE_COMMENTS)
    pct = random.randint(60, 99)
    print_delay(f"\n❤️ Compatibility: {pct}%")
    print_delay(f"💬 {love}")
