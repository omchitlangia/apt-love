# utils/win_screen.py
import time
import os
from blessed import Terminal
from utils.printer import print_delay

term = Terminal()

def show_win_screen(score):
    frames = [
        [
            "     ♥            ♥",
            "         ♥   YOU   ♥",
            "     ♥   FOUND LOVE! ♥",
            "         ♥         ♥"
        ],
        [
            "         ♥         ♥",
            "     ♥   TRUE MATCH!  ♥",
            "         ♥         ♥",
            "     ♥           ♥"
        ],
        [
            "     💘   💘   💘   💘",
            "         YOU WON!",
            "     💘   💘   💘   💘"
        ]
    ]

    print(term.clear)
    print_delay("\n💖 Score Milestone Achieved! Launching Win Screen...\n", 0.02)

    colors = [term.red, term.magenta, term.yellow]

    for _ in range(5):  # Number of animation cycles
        for frame in frames:
            print(term.move_y(5))  # vertical padding
            color = colors[_ % len(colors)]
            print(term.clear)
            for line in frame:
                print(color(line.center(term.width)))
            print(term.cyan(f"\n🏆 Final Score: {score}".center(term.width)))
            time.sleep(0.4)
