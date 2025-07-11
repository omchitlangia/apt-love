import time
import random
import sys

GREEN = "\033[92m"
RESET = "\033[0m"
GREY = "\033[90m"
BOLD = "\033[1m"


def print_delay(text, delay=0.02, newline=True):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    if newline:
        print()


def boot_sequence():
    print("\033c", end='')  # clear screen
    print_delay(f"{GREY}[    0.000000] Booting Linux kernel 5.15.0-generic{RESET}")
    time.sleep(0.2)

    messages = [
        "Initializing hardware timer...",
        "Loading kernel modules...",
        "Mounting /proc...",
        "Mounting /dev...",
        "Mounting /sys...",
        "Starting udevd daemon...",
        "Loading device drivers...",
        "Bringing up network interfaces...",
        "Starting systemd services...",
        "Reached target Multi-User Mode."
    ]

    for i, msg in enumerate(messages):
        ts = round(random.uniform(0.01, 0.2) + i * 0.02, 6)
        status = f"{GREEN}OK{RESET}"
        print_delay(f"{GREY}[    {ts}] {msg}{RESET} {status}")
        time.sleep(0.15)

    print()
    print_delay(f"{BOLD}Linux v1.0 machine tty1{RESET}")
    print_delay("\nlogin: root", delay=0.01)
    print_delay("Password: ********\n", delay=0.02)
    print_delay(f"{BOLD}Welcome to Linux v1.0 (-generic x86_64){RESET}")
    print_delay("\nTo run a command as administrator (user 'root'), use 'sudo <command>'.")
    print_delay("See 'man sudo_root' for details.\n")
    print_delay("root@main:~# ", delay=0.01, newline=False)


if __name__ == '__main__':
    boot_sequence()
