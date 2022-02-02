"""The Hangman is a simple game in which the player should guess the randomly generated word.
Player can choose a game difficulty which says how may times player can try to guess the word:
entry level - 7 tries
intermediate level - 5 tries,
professional level - 3 tries.
The word is represented by a row of dashes. Player suggest a letter, if the letter doesn't occur in the word, player
 loses one of his tries. Player can try to guess a letter as long as the number of tries raises 0. If the player guess
 all the letter from the word, wins."""

import random
import sys
import pyinputplus as pyip


file = r'word_hangman.txt'
number_of_tries = pyip.inputMenu(['entry', 'intermediate', 'professional'], 'Select a difficulty level: \n',
                                 numbered=True, )


def random_word(filename):
    with open(filename, mode='r') as f:
        line = f.readline().split(', ')
        word = random.choice(line)
        return word


class Hangman:
    def __init__(self, word, level):
        self.word = word
        self.level = level

    def choose_difficulty(self):  # choosing number of tries
        difficulty_level = {'entry': 7, 'intermediate': 5, 'professional': 3}
        chance = difficulty_level[self.level]
        return chance

    def hidden_word(self):  # putting dash instead of letter
        user_word = []
        for letter in self.word:
            user_word.append('_')
        return user_word

    def show_game_status(self, chance, user_word):
        print(f"{''.join(user_word)}")
        if chance == 1:
            print(f'You have the last chance!')
        elif chance > 1:
            print(f'You have {chance} tries.')

    def find_indexes(self, letter):
        indexes = []
        for index, user_letter in enumerate(self.word):
            if user_letter == letter:
                indexes.append(index)
        return indexes

    def play_game(self):
        user_letters = []
        user_words_result = self.hidden_word()
        chance = self.choose_difficulty()
        print(f"Word to guess: {''.join(user_words_result)}")
        while True:
            user_letter = pyip.inputStr('Give a letter: ')
            if user_letter in user_letters:
                print("You've used this letter, please give another letter: ")
            user_letters.append(user_letter)
            founded_indexes = self.find_indexes(user_letter)
            if len(founded_indexes) == 0:
                print('There is no such letter!')
                chance -= 1
                if chance == 0:
                    print('Game Over!')
                    break
            else:
                for index in founded_indexes:
                    user_words_result[index] = user_letter

                if ''.join(user_words_result) == self.word:
                    print('You won!!!')
                    break
            self.show_game_status(chance, user_words_result)


while True:
    Hangman(random_word(file), number_of_tries).play_game()
    message = pyip.inputYesNo('Do you like to play again?')
    print(message)
    if message == 'yes':
        continue
    else:
        sys.exit(0)



