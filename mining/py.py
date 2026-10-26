
import random
import subprocess
import time
import pyperclip

words = [
    "hello",
    "computer",
    "artificial intelligence",
    "Python",
    "bonjour",
    "नमस्ते",
    "こんにちは",
    "technology",
    "universe",
    "programming",
]

print("Focus the target text field within 5 seconds.")
print("Press Ctrl+C in this terminal to stop.")
time.sleep(10)

try:
    while True:
        word = random.choice(words)
        pyperclip.copy(word)

        subprocess.run(
            ["xdotool", "key", "--clearmodifiers", "ctrl+v"],
            check=True
        )
        subprocess.run(
            ["xdotool", "key", "Return"],
            check=True
        )

        print(f"Sent: {word}")
        time.sleep(15)

except KeyboardInterrupt:
    print("\nStopped.")
