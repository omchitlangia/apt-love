# games/date_invaders.py
try:
    import curses
except ImportError:
    import os
    os.system("pip install windows-curses")
    import curses

import random
import time
import os
import json
from utils.printer import print_delay
from utils.win_screen import show_win_screen

ENEMIES = ["👻", "🚩", "😬", "📸", "💅", "❤‍🩹"]
BONUSES = ["🐧", "📓", "🧠"]
HEARTBREAK_QUOTES = {
    "👻": "💔 They ghosted you and your messages... brutal.",
    "🚩": "🚩 Red flag alert. And you walked right into it.",
    "😬": "😬 They quoted Fight Club on the first date. Yikes.",
    "📸": "📸 All profile pics are 3rd-wheel selfies. Uh oh.",
    "💅": "💅 Crypto bro wants to DM you his pitch deck.",
    "❤‍🩹": "❤‍🩹 Your emotionally unavailable ex matched again..."
}

SCORE_FILE = "data/scores.json"

class Projectile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class FallingObject:
    def __init__(self, x, y, char, is_bonus=False):
        self.x = x
        self.y = y
        self.char = char
        self.is_bonus = is_bonus

def save_score(username, score):
    os.makedirs("data", exist_ok=True)
    if os.path.exists(SCORE_FILE):
        with open(SCORE_FILE, "r") as f:
            scores = json.load(f)
    else:
        scores = []
    scores.append({"user": username, "score": score})
    scores = sorted(scores, key=lambda x: x["score"], reverse=True)[:5]
    with open(SCORE_FILE, "w") as f:
        json.dump(scores, f, indent=2)

def get_high_score():
    if os.path.exists(SCORE_FILE):
        with open(SCORE_FILE, "r") as f:
            scores = json.load(f)
            if scores:
                return scores[0]["score"]
    return 0

def start_date_invaders():
    curses.wrapper(main_game_loop)

def main_game_loop(stdscr):
    try:
        with open("data/profile.json") as pf:
            username = json.load(pf).get("username", "Anonymous")
    except:
        username = "Anonymous"

    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.timeout(0)

    max_y, max_x = stdscr.getmaxyx()
    game_height = min(50, max_y)
    game_width = min(30, max_x)
    player_x = game_width // 2

    lives = 3
    score = 0
    projectiles = []
    enemies = []
    tick = 0
    recent_quotes = [""]
    quote_timer = 0
    quote_display_duration = 20
    floaters = []
    paused = False
    explosions = []

    def draw_border():
        stdscr.border()

    def display_info():
        stdscr.addstr(0, 2, f"♥ Lives: {lives}  💘 Score: {score}  Press 'q' to quit | 'p' to pause")

    def spawn_enemy():
        char = random.choice(ENEMIES + BONUSES)
        x = random.randint(1, game_width - 3)
        enemies.append(FallingObject(x, 1, char, char in BONUSES))

    def draw():
        stdscr.clear()
        draw_border()
        display_info()
        stdscr.addstr(game_height - 2, player_x - 1, "♥" * lives if lives <= 3 else "♥♥♥")
        if paused:
            stdscr.addstr(game_height // 2, game_width // 2 - 6, "⏸️ PAUSED ⏸️")
        for e in enemies:
            if 1 <= e.y < game_height - 1:
                stdscr.addstr(e.y, e.x, e.char)
        for p in projectiles:
            stdscr.addstr(p.y, p.x, "↑")
        for x, y, txt, timer in floaters:
            if timer > 0 and 1 < y < game_height - 2:
                stdscr.addstr(y, x, txt)
        for x, y, timer in explosions:
            if timer > 0:
                stdscr.addstr(y, x, "💥")
        if recent_quotes[-1] and quote_timer > 0:
            stdscr.hline(game_height - 1, 1, curses.ACS_HLINE, game_width - 2)
            quote_lines = [recent_quotes[-1][i:i + game_width - 4] for i in range(0, len(recent_quotes[-1]), game_width - 4)]
            for i, line in enumerate(quote_lines[-2:]):
                if game_height - 3 + i < max_y - 1:
                    stdscr.addstr(game_height - 3 + i, 2, line)
        stdscr.refresh()

    def update_projectiles():
        for p in projectiles[:]:
            p.y -= 1
            if p.y < 1:
                projectiles.remove(p)

    def update_enemies():
        nonlocal lives, quote_timer
        for e in enemies[:]:
            e.y += 1
            if e.y >= game_height - 2:
                if not e.is_bonus:
                    curses.beep()
                    lives -= 1
                    quote = HEARTBREAK_QUOTES.get(e.char, "💔 You've been emotionally compromised.")
                    recent_quotes.clear()
                    recent_quotes.append(quote)
                    quote_timer = quote_display_duration
                enemies.remove(e)

    def handle_collisions():
        nonlocal score, lives
        hits = []
        for p in projectiles[:]:
            for e in enemies[:]:
                if abs(p.x - e.x) <= 2 and abs(p.y - e.y) <= 1:
                    hits.append((p, e))
        for p, e in hits:
            explosions.append((e.x, e.y, 3))
            if e.is_bonus:
                lives = min(lives + 1, 3)
                score += 20
                floaters.append((e.x, e.y, "+20 ❤️", 4))
            else:
                score += 10
                floaters.append((e.x, e.y, "+10", 4))
            if e in enemies:
                enemies.remove(e)
            if p in projectiles:
                projectiles.remove(p)

    def update_floaters():
        updated = []
        for x, y, txt, timer in floaters:
            if timer > 0:
                updated.append((x, y - 1, txt, timer - 1))
        floaters.clear()
        floaters.extend(updated)

    def update_explosions():
        updated = []
        for x, y, timer in explosions:
            if timer > 0:
                updated.append((x, y, timer - 1))
        explosions.clear()
        explosions.extend(updated)

    print_delay("\nLaunching 💘 Date Invaders...", 0.02)
    time.sleep(0.3)

    while lives > 0:
        key = stdscr.getch()
        if key == ord('p'):
            paused = not paused
        if paused:
            draw()
            time.sleep(0.1)
            continue

        if score >= 1000:
            show_win_screen(score)
            break
        if key in [ord('q'), ord('Q')]:
            break
        elif key == curses.KEY_LEFT and player_x > 2:
            player_x -= 1
        elif key == curses.KEY_RIGHT and player_x < game_width - 3:
            player_x += 1
        elif key == ord(' '):
            projectiles.append(Projectile(player_x, game_height - 3))
        elif key == ord('l'):
            enemies.clear()

        if tick % 20 == 0:
            spawn_enemy()

        update_projectiles()
        update_enemies()
        handle_collisions()
        update_floaters()
        update_explosions()
        draw()
        tick += 1
        if quote_timer > 0:
            quote_timer -= 1

        time.sleep(0.15)

    stdscr.clear()
    stdscr.addstr(game_height//2 - 2, 5, "💔 You've been emotionally compromised!")
    stdscr.addstr(game_height//2, 5, f"Your final score: {score}")
    high_score = get_high_score()
    stdscr.addstr(game_height//2 + 1, 5, f"🏆 Highest score: {high_score}")
    save_score(username, score)
    stdscr.addstr(game_height//2 + 3, 5, "Press any key to return to apt-love")
    stdscr.refresh()
    time.sleep(5)
    stdscr.getch()
