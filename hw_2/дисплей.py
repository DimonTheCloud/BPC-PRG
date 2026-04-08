import json

def load_pics(filename = "hangman_1.json"):
    with open(filename, "r", encoding= "utf-8") as file:
        pics = json.load(file)


def show_welcome_message():
    print("Добро пожаловать в игру Виселица!\nТебе нужно угадывать слово по буквам.")

def show_game_state(game_state, pics, failed_attempts, used_chars):
    print(pics[failed_attempts])
    print(f"Word:", game_state)
    if used_chars:
        print(f"Used letters:", ", ".join(used_chars))
    else:
        print(f"Used letters: none")

def show_feedback(is_correct):
    if is_correct:
        print("Right!")
    else:
        print("Wrong!")

def show_game_over(is_win, secret_word):
    if is_win == True:
        print(f"Hooray! You won!")
        print(f"Secret Word was: {secret_word}")
    elif is_win == False:
        print(f"Sorry, you lost!")
        print(f"Secret Word was: {secret_word}")





