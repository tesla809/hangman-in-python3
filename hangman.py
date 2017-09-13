# re-factor:
# re-factor extract random word choice code
# re-factor code to extract case correction code outside word update
# draw hangman function
"""
Hangman in Python (beta)
by Anthony Albertorio
9/11/17
"""
import random

words = ['Hello', 'world', 'United', 'America', 'Korea', 'cars', 'jazz']


def hangman_draw(count):
    head = '            |'
    torso = '               |'
    left_arm = ''
    right_arm = '     '
    left_leg_1 = '              |'
    left_leg_2 = '              |'
    right_leg_1 = ' '
    right_leg_2 = '  '

    if count >= 1:
        head = 'O           |'
    if count >= 2:
        torso = '   |           |'
    if count >= 3:
        torso = '|           |'
        left_arm = 'o--'
    if count >= 4:
        torso = '|'
        left_arm = 'o--'
        right_arm = '--o        |'
    if count >= 5:
        left_leg_1 = ' /            |'
        left_leg_2 = '/             |'
    if count >= 6:
        left_leg_1 = ' /'
        left_leg_2 = '/'
        right_leg_1 = '\\          |'
        right_leg_2 = '  \\         |'

    print("""
         ____________ 
        |           |
        {0}
     {2}{1}{3}
      {4} {6}
      {5} {7}
                    |
                    |
               _________
              |         |
              |_________|
    """.format(head, torso, left_arm, right_arm,
               left_leg_1, left_leg_2,
               right_leg_1, right_leg_2))


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
                # probelm is here
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
    # choice gets random element from iterable
    random_word = random.choice(word_list)
    guess_count = 6
    countdown = 0
    hidden_word = '_' * len(random_word)
    letters_inputed_list = []
    output_word = space_maker(hidden_word)

    # output initial word hint
    print('{0} letters: {1}'.format(len(hidden_word), output_word))

    while guess_count > 0:
        # reveals word to test
        # print(random_word)
        # check if done
        if '_' not in hidden_word:
            print('All done!')
            break

        # draw
        hangman_draw(countdown)
        # get input
        user_guess = input('Guess a letter: ')
        if user_guess not in letters_inputed_list:
            letters_inputed_list.append(user_guess)
            if word_update(hidden_word, random_word, user_guess) != None:
                hidden_word = word_update(hidden_word, random_word, user_guess)
                output_word = space_maker(hidden_word)
                # draw
                hangman_draw(countdown)
                print(output_word)
            else:
                guess_count -= 1
                # counter up letter
                countdown += 1
                print('You have {0} guesses'.format(guess_count))
        else:
            print('You guessed that letter. Try again.')


game(words)