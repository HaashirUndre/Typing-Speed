import time
import random
from colorama import Fore, Style, init
init(autoreset=True, convert=True)

# Initialize colorama for color output in terminal
init(autoreset=True)

def type_effect(text: str, delay: float = 0.02):
    for ch in text:
        print(ch, end='', flush=True)
        time.sleep(delay)
    print()

# Sentence bank for random selection
SENTENCES = [
    "Discipline beats motivation every single day.",
    "Every expert was once a beginner who didnt quit.",
    "Clean code is not written faster, its written better.",
    "Focus on consistency over intensity.",
    "Small progress each day adds up to big results.",
    "Your only limit is the one you set yourself.",
    "Dream big, work hard, stay humble.",
    "Code like you mean it, debug like you care.",
    "The best error message is the one that never shows up.",
    "Quality is not an act, its a habit."
]
# Runs the program
def typing_speed_test():
    type_effect(Fore.WHITE + "---Welcome to TYPING SPEED TEST---")
    print(Fore.YELLOW + "Type the given sentence as fast and accurately as possible.\n")
    input(Fore.MAGENTA + "Press Enter when youre ready... ")

    # Pick a random sentence
    sentence = random.choice(SENTENCES)
    print("\n" + Fore.CYAN + "Your sentence:\n" + Style.BRIGHT + sentence)
    input(Fore.MAGENTA + "\nPress Enter to start typing... ")

    # Start timer
    start_time = time.time()
    user_input = input(Fore.WHITE + "\nStart typing here:\n")
    end_time = time.time()

    # Calculate stats
    time_taken = end_time - start_time
    words = len(sentence.split())
    wpm = (words / time_taken) * 60

    correct_chars = sum(1 for i in range(min(len(sentence), len(user_input))) if sentence[i] == user_input[i])
    accuracy = (correct_chars / len(sentence)) * 100

    # Display results
    print("\n" + Fore.GREEN + "========== RESULTS ==========")
    print(Fore.YELLOW + f"Time Taken : {time_taken:.2f} sec")
    print(Fore.YELLOW + f"Speed       : {wpm:.2f} WPM")
    print(Fore.YELLOW + f"Accuracy    : {accuracy:.2f}%")

    # Performance feedback
    if wpm < 30:
        print(Fore.RED + "Thats awfully bad but keep practicing.")
    elif wpm < 60:
        print(Fore.MAGENTA + "Nice work! Youre improving steadily.")
    elif wpm < 90:
        print(Fore.GREEN + "Great job! Thats solid typing speed.")
    else:
        print(Fore.CYAN + "Outstanding! Youre typing like a professional.")

if __name__ == "__main__":
    typing_speed_test()
