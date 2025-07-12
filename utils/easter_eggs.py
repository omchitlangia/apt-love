from utils.printer import print_delay
import random

def run_easter_egg(cmd):
    if cmd == "whoami":
        print_delay("🧠 root@love-machine")
    elif cmd == "uname -a":
        print_delay("Linux LoveOS 4.20.69 #1 SMP PREEMPT x86_64 GNU/Linux ❤️")
    elif cmd == "curl ifconfig.me":
        print_delay("127.0.0.1 — You're always home to me.")
    elif cmd == "history":
        print_delay("1  sudo apt install love\n2  echo 'it’s complicated'\n3  start-dating")
    elif cmd == "sudo !!":
        print_delay("sudo sudo apt install love\n💥 Recursive love loop initiated...")
    elif cmd == "man love":
        print_delay("LOVE(1) — Linux User's Very Emotional command manual\n\nSYNOPSIS\n    love [--unconditional] [--open-heart]\n\nDESCRIPTION\n    Spreads kindness, matches soulmates, and compiles emotions.\n")
    else:
        print_delay("🤖 Unknown command. Type help for supported commands.")
