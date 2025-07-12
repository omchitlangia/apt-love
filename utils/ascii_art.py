import time
import os
from utils.printer import print_delay

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_match_animation():
    frames = [
        r"""
         💘        💘
       💘   💘  💘   💘
         💘        💘
        """,
        r"""
       💘        💘
     💘   💘  💘   💘
       💘        💘
        """,
        r"""
     💘        💘
   💘   💘  💘   💘
     💘        💘
        """,
    ]

    for i in range(3):
        for frame in frames:
            clear()
            print(frame)
            time.sleep(0.3)

    print_delay("\n💖 IT’S A MATCH! 💖\n", delay=0.04)
