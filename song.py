import time
import sys

def print_lyrics():
    lyrics = [
        "Jeene laga hoon, pehle se zyada",
        "Pehle se zyada tumpe marne laga hoon",
        "Main mera dil aur tum ho yahan",
        "Phir kyun ho palkein jhukayein wahan",
        "Tum sa haseen pehle dekha nahin",
        "Tum isse pehle the jaane kahan",
        "Jeene laga hoon pehle se zyada",
        "Pehle se zyada..."
    ]

    # pause after each printed line (seconds) — tuned to approximate the song
    delays = [2.4, 1.8, 2.2, 1.9, 1.6, 1.8, 2.4, 1.6]

    # typing speed per character (seconds). Lower => faster typing.
    typing_delay = 0.06

    # Opening line (changed to song title)
    print("Jeene laga hoon...\n")
    time.sleep(1.0)

    for i, line in enumerate(lyrics):
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(typing_delay)
        print()                  # newline after the line
        # wait before next line (use delays list; fallback if index missing)
        pause = delays[i] if i < len(delays) else 1.5
        time.sleep(pause)

if __name__ == "__main__":
    print_lyrics()