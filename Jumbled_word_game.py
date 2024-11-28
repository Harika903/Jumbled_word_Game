import tkinter as tk
import random
import ttkbootstrap as tb


# Global variables
current_score=0
current_word = ""
current_hint = ""
current_difficulty = ""

# Word sets for different difficulty levels
word_sets = {
    "simple": {
        "cat": "A small domesticated carnivorous mammal.",
        "dog": "A domesticated carnivorous mammal with four legs.",
        "crow": "often seen bird in india.",
        "monkey": "seen in forests known for its mischevious behaviour.",
        "goat": "Domestic animal commonly found in rural areas."
    },
    "medium": {
        "elephant": "A large herbivorous mammal with a trunk.",
        "giraffe": "A tall, long-necked mammal native to Africa.",
        "cheetah": "Fastest land animal,known for its incredible speed .",
        "ostrich": "Flightless bird  known for being larges of all birds.",
        "deer": "Herbivore with antlers found in forests and meadows."

    },
    "difficult": {
        "hippopotamus": "A large herbivorous mammal with thick skin.",
        "rhinoceros": "A large herbivorous mammal with one or two horns.",
        "peacock": "National bird of india.",
        "fossa": "Canivorous animal native to madagascar.",
        "platypus": "unique mammal native to australia."
    }
}

def pick_word(difficulty):
    global current_word, current_hint
    current_word, current_hint = random.choice(list(word_sets[difficulty].items()))
    reset_button.config(state="disabled")
    return current_word

def show_hint():
    global current_hint
    hint_label.config(text=f"Hint: {current_hint}")

def jumble_word(word):
    jumbled = ''.join(random.sample(word, len(word)))
    return jumbled

def display_word(difficulty):
    hint_label.config(text="")
    global current_difficulty
    current_difficulty = difficulty
    word = pick_word(difficulty)
    jumbled = jumble_word(word)
    jumbled_label.config(text=jumbled)
    show_page("game")

def check_word():
    global current_score
    user_input = entry.get()
    if user_input.lower() == current_word.lower():
        result_label.config(text="Correct!")
        current_score += 1
        reset_button.config(state="normal")
        update_score_label()
    else:
        result_label.config(text="Incorrect. Try again.")
        reset_button.config(state="disabled")


def next_word():
    global current_score
    entry.delete(0, tk.END)
    display_word(current_difficulty)
    result_label.config(text="")
    reset_button.config(state="disabled")


def update_score_label():
    score_label.config(text=f"Score: {current_score}")


def show_page(page):
    if page == "intro":
        intro_frame.pack()
        game_frame.pack_forget()
    elif page == "game":
        intro_frame.pack_forget()
        game_frame.pack()

def start_game():
    show_page("game")
    display_word("simple")


root = tb.Window(themename="vapor")
root.geometry("600x600")
root.title("Jumbled Word Game")

# Frame for introduction
intro_frame = tb.Frame(root)

intro_frame.pack(pady=50)

# Labels and button for introduction
intro_label = tb.Label(intro_frame, text="Jumbled Word\n       Game",font=("Arial",30))
intro_label.pack(pady=40)

enter_button = tb.Button(intro_frame, text="Enter",width=30,command=start_game)
enter_button.pack(pady=60)

# Frame for game
game_frame = tb.Frame(root)
# Frame for difficulty level buttons
difficulty_frame = tb.Frame(game_frame)
difficulty_frame.pack(pady=10)

# Buttons for difficulty levels
btn_simple = tb.Button(difficulty_frame, text="Simple", width=10,command=lambda: display_word("simple"))
btn_medium = tb.Button(difficulty_frame, text="Medium", width=10,command=lambda: display_word("medium"))
btn_difficult = tb.Button(difficulty_frame, text="Difficult",width=10, command=lambda: display_word("difficult"))

btn_simple.grid(row=0, column=0, padx=10)
btn_medium.grid(row=0, column=1, padx=10)
btn_difficult.grid(row=0, column=2, padx=10)

# Frame for jumbled word display and user input
jumbled_frame = tb.Frame(game_frame)
jumbled_frame.pack(pady=20)

jumbled_label = tb.Label(jumbled_frame, font=("Arial", 18))
jumbled_label.pack()

entry = tb.Entry(jumbled_frame, font=("Arial", 12))
entry.pack(pady=10)

result_label = tb.Label(jumbled_frame, font=("Arial", 12))
result_label.pack()

score_label=tb.Label(game_frame,text="Score: 0",font=("Arial",12))
score_label.pack()


hint_label = tb.Label(jumbled_frame, font=("Arial", 12))
hint_label.pack()

# Buttons for hint, check, and reset
hint_button = tb.Button(game_frame, width=30,text="Hint", command=show_hint)
hint_button.pack(pady=5)

check_button = tb.Button(game_frame, width=30,text="Check", command=check_word)
check_button.pack(pady=5)

reset_button = tb.Button(game_frame, width=30,text="Next", command=next_word)
reset_button.pack(pady=5)

root.mainloop()