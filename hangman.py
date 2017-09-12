# re-factor:
# extract random word choice code
# code to extract case correction code outside word update
# draw hangman function
# add ability to query dictionary api to get random word.

"""
Hangman in Python (beta)
by Anthony Albertorio
9/11/17
"""
import random

words = ['Hello', 'world', 'United', 'America', 'Korea', 'cars', 'jazz']


def get_random_word(word_list):
    # get random word index. -1 because randint is inclusive of end value
    random_word_index = random.randint(0, len(word_list) - 1)
    random_word = word_list[random_word_index].lower()
    return random_word


def duplicates(lst, item):
    return [i for i, x in enumerate(lst) if x == item]


def space_maker(word):
    word = list(word)
    word_space = ['{0} '.format(elem) for elem in word]
    return ''.join(word_space)


def word_update(hidden_word, random_word, guess_letter):
    # checks if letters
    if guess_letter.isalpha():
        # correct if user uses upper case
        guess_letter = guess_letter.lower()
        hidden_word_list = list(hidden_word)
        upper_case_list = []

        # handle upper case letters
        for letter in random_word:
            if letter.isupper():
                # create list where upper case letters are
                upper_case_list = duplicates(list(random_word), letter)
        random_word = random_word.lower()

        # find duplicate letters
        matched_values = duplicates(random_word, guess_letter)

        # replace letter
        if len(matched_values) != 0:
            for letters in matched_values:
                # problem is here
                hidden_word_list[letters] = guess_letter
            # place back letter case
            for upper_case in upper_case_list:
                upper_case_letter_index = upper_case_list[upper_case]
                letter = random_word[upper_case_letter_index]
                letter_case_corrected = letter.upper()
                hidden_word_list[upper_case_letter_index] = letter_case_corrected

            # if all good return updated word
            updated_word = ''.join(hidden_word_list)
            return updated_word
        else:
            print('{0}: not matching'.format(guess_letter))

    else:
        print('{0}: not valid letters'.format(guess_letter))
    # if not good return None
    return None


def game(word_list):
    random_word = get_random_word(word_list)
    guess_count = 5
    hidden_word = '_' * len(random_word)
    letters_inputed_list = []
    output_word = space_maker(hidden_word)

    while guess_count > 0:
        # reveals word to test
        # print(random_word)
        # check if done
        if '_' not in hidden_word:
            print('All done!')
            break

        # output initial word hint
        print('\n{0} letters: {1}'.format(len(hidden_word), output_word))
        # get input
        user_guess = input('Guess a letter: ')
        if user_guess not in letters_inputed_list:
            letters_inputed_list.append(user_guess)
            if word_update(hidden_word, random_word, user_guess) != None:
                hidden_word = word_update(hidden_word, random_word, user_guess)
                output_word = space_maker(hidden_word)
                print(output_word)
            else:
                guess_count -= 1
                print('You have {0} guesses'.format(guess_count))
        else:
            print('Try again. letter there already\n')
    else:
        print('You lost!\n')

game(words)
