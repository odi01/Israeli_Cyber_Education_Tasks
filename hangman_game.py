import string
import os.path


HANGMAN_PHOTOS = {
        1:
            """
    x-------x
    """,

        2:
            """
    x-------x
    |
    |
    |
    |
    |
    """,

        3:
            """
    x-------x
    |       |
    |       0
    |
    |
    |
    """,

        4:
            """
    x-------x
    |       |
    |       0
    |       |
    |
    |
    """,

        5:
            """
    x-------x
    |       |
    |       0
    |      /|\\
    |
    |
    """,

        6:
            """
    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |
    """,

        7:
            """
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |
    """,
    }


def welcome_screen():
    """Print the welcome screen of the game"""

    HANGMAN_ASCII_ART = """
    Welcome to the game Hangman
      _    _
     | |  | |
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
     |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \\
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                          __/ |
                         |___/

    """

    MAX_TRIES = 6

    print(HANGMAN_ASCII_ART, MAX_TRIES, "\n")


def print_hangman(num_of_tries, hangman_status):
    """
    Print the status of the user failed attempts
    :return: Key in the dictionary
    :rtype: dict
    """
    try:
        print(hangman_status[num_of_tries])

    except KeyError:
        print('ERROR')


def user_input():
    """
    User file path location and the position of a word in the file
    file_path(type: str) - the path for the txt file
    index(type: int) - the position of the word in the txt file.
    :return: The file path that contain words and an index of a specific word in the file
    :rtype: file_path(str), index(int)
    """
    words_file_path = input(r"Enter file path: ")

    # Check if file path exist
    while os.path.exists(words_file_path) is False:
        print("Wrong file path, try again\n")
        words_file_path = input(r"Enter file path: ")

    word_index_in_file = input("Enter index: ")

    # Check if index input is a vaild number
    while True:
        try:
            int(word_index_in_file)
        except ValueError:
            # Not a valid number
            print("You must enter a number\n")
            word_index_in_file = input("Enter index: ")
        else:
            word_index_in_file = int(word_index_in_file)
            break

    return words_file_path, word_index_in_file


def choose_word(file_path, index):
    """
    Generate a secret word from a file that contains words that are separated by spaces,
    by choosing a file path and an index of a word in the file.

    :param index: The position of the word in the txt file
    :type file_path: str
    :type index: int
    :return: a secrect word that the user chose and don't know which base
    on the index decision that he made.
    :rtype: str
    """

    secret_word = ""
    with open(file_path, 'r') as words_file:
        # Step 1 - Find the unique words number (remove duplicates)
        # Convert string to list to create from each word an item
        words_file_list = words_file.read().split(" ")

        # Step 2 - Return a word base on index number
        # Case 1 - Index input is two times bigger at most than list length
        # in this case just iterate the word file one more time
        if len(words_file_list) < index:
            updated_index = index - len(words_file_list)
            try:
                secret_word += words_file_list[updated_index - 1]

            # Case 1.2 - Index is 2^∞ bigger than list length
            except IndexError:
                updated_index_two = updated_index - len(words_file_list)
                # Subtract each run list length from index.
                while updated_index_two > len(words_file_list):
                    updated_index_two -= len(words_file_list)
                secret_word += words_file_list[updated_index_two - 1]

        # Case 2 - Ideal case - index is smaller than list length
        else:
            secret_word += words_file_list[index - 1]

    return secret_word


def check_valid_input(letter_guessed, old_letters_guessed):
    """
    Check letter input validation by return Boolean value,
    return False when letter_guessed contain:
    A. More than two characters.
    B. Non English letters. ($%^&#15)
    C. Character that already in old_letters_guessed = user was already guessed it.
    D. Guessed letter isn't number

    :param letter_guessed: user input letter
    :param old_letters_guessed: letter that the user was already guessed
    :type letter_guessed: str
    :type old_letters_guessed: str
    :return: True/False if the user input is valid.
    :rtype: boolean
    """

    # Case 1 - Value bigger than one
    if len(letter_guessed) > 1:
        return False

    # Case 2 - Letter contain non-English characters
    elif (letter_guessed.translate(string.punctuation).isalnum()) is False:
        return False

    # Case 3 - Letter was already guessed
    elif letter_guessed in old_letters_guessed:
        return False

    # Case 4 - Input is int or valid
    else:
        try:
            val = int(letter_guessed)  # Try to convert to int
            return False

        except ValueError:  # Valid input
            return True


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    Using "check_valid_input" function to find if the guess letter is valid.
    If guess letter is invalid the function print "X" and below the letters
    that the player already guessed separated by "->" sort from A-Z.
    If guess letter is valid  the function add the letter to the guessed letters list.

    :param letter_guessed: user input letter
    :param old_letters_guessed: letter that the user was already guessed

    :type letter_guessed: str
    :type old_letters_guessed: str
    """

    # arrow sign to add for a False return
    arrow_sign = " -> "

    # Case 1 - Valid input
    if check_valid_input(letter_guessed, old_letters_guessed) is True:
        old_letters_guessed.append(letter_guessed)

    # Case 2 - Invalid input
    else:
        print("X\n invalid input")
        old_letters_guessed.sort()  # Sort the letter from a-z
        arrow = (arrow_sign.join(old_letters_guessed))  # convert the list to str + adding the arrow sign
        print(arrow)


def show_hidden_word(secret_word, old_letters_guessed):
    """
    Return a string that built from letters and underlines "_".
    The string represent the letters from old_letters_guessed that are in secret_word
    and their index, and the rest of the letters is the string which the player didn't
    guess as underlines.

    :param secret_word: Player selected word
    :param old_letters_guessed: All the letters that the player guessed

    :type secret_word: str
    :type old_letters_guessed: list

    :return: The secret word in the hidden format.
    :rtype: str
    """

    hidden_word = ""

    for letter in secret_word:
        hidden_word += " _ "

    # How many times guessed_letter appears in secret_word
    occurrences = []
    for guessed_letter in old_letters_guessed:
        for i, letter in enumerate(secret_word):
            if letter == guessed_letter:
                occurrences.append(i)

    hidden_word = list(hidden_word)  # Convert to list for item assignment

    for index in occurrences:
        hidden_word[(index * 3) + 1] = secret_word[index]  # (x*3 + 1) - Due to white spaces

    hidden_word = "".join(hidden_word)  # Convert back to string
    return hidden_word


def check_win(secret_word, old_letters_guessed):
    """
    Check player win by finding if all guess letters are in secret word.

    :param secret_word: Player selected word
    :param old_letters_guessed: All the letters that the player guessed

    :type secret_word: str
    :type old_letters_guessed: list

    :return: True if all old_letters_guessed are in secret_word, else False
    :rtype: Boolean
    """

    result = []
    for letter in secret_word:
        if letter in old_letters_guessed:
            result.append(True)
        else:
            result.append(False)

    SecretWord_contains_all_letters = all(result)  # Search for a False item in result list

    return SecretWord_contains_all_letters


def main():
    welcome_screen()
    words_file_path, word_index = user_input()
    secret_word = choose_word(words_file_path, word_index)
    print("\nLet’s start!")
    num_of_tries = 1
    print_hangman(num_of_tries, HANGMAN_PHOTOS)
    already_guessed_letters = []

    while num_of_tries <= 6:
        hidden_word = show_hidden_word(secret_word, already_guessed_letters)
        print(hidden_word, "\n")

        guess_letter = input("Guess a letter: ").lower()
        while "" == guess_letter:  # Prevent count white spaces as a word
            guess_letter = input("Guess a letter: ").lower()

        # Valid word but wrong guess
        if check_valid_input(guess_letter, already_guessed_letters) is True \
                and guess_letter not in secret_word:
            num_of_tries += 1
            print_hangman(num_of_tries, HANGMAN_PHOTOS)
        else:
            pass

        try_update_letter_guessed(guess_letter, already_guessed_letters)

        # Win
        if check_win(secret_word, already_guessed_letters) is True:
            print("WIN \n The secret word was: {}".format(secret_word))
            break
        else:
            pass

    # Loss
    if num_of_tries == 7:
        print("LOSE \n The secret word was: {}".format(secret_word))


if __name__ == '__main__':
    main()
