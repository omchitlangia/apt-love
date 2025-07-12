import random
from utils.printer import print_delay

QUOTES = [
    "Are you a Bash shell? Because you autocomplete me.",
    "My love for you is like a while(true) loop — it never ends.",
    "You're the sudo to my root access.",
    "I'd grep the entire internet just to find you.",
    "Your eyes sparkle brighter than my RGB terminal.",
    "You must be running top — because you're taking all my resources.",
    "If you were a package, I'd install you with no dependencies.",
    "Our love is like Git — distributed but in sync.",
    "Even Emacs and Vim agree you're amazing.",
    "You reboot my heart every time you smile.",
    "You must be chmod 777 — because you have full access to my heart.",
    "I'd commit to you without even staging my feelings.",
    "You're the localhost to my 127.0.0.1 ❤️"
]

def show_random_quote():
    quote = random.choice(QUOTES)
    print_delay(f"\n💌 {quote}\n", delay=0.03)
