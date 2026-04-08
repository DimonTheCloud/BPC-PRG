import random

def choose_word(words):
    return random.choice(words)

def get_user_char(used_chars):
    while True:
        user_char = input(f"Please enter your letter: ")

        if not user_char.isalpha():
            print("Please enter a letter")
            continue

        if len(user_char) != 1:
            print("Please enter a ONE letter")
            continue

        if user_char in used_chars:
            print("This letter already used")

        used_chars.append(user_char)
        return user_char, used_chars

def replace_chars(game_state, used_char, secret_word):
    updated_state = ""

    for i in used_char:
        if secret_word[i] == used_char:
            updated_state += used_char
        else:
            updated_state += game_state[i]

    return updated_state