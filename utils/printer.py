import time

def print_delay(text, delay=0.02, newline=True):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    if newline:
        print()
