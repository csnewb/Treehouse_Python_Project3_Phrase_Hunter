# Create your Game class logic in here.
import string
from phrasehunter import phrase
import settings
import random

class Game():
    def __init__(self):
        self.missed = 0
        self.phrases = self.create_phrases()
        self.active_phrase = self.get_random_phrase(self.phrases)
        self.guesses = []

    def create_phrases(self):
        choices = random.choices(settings.phrase_pool, k=5)
        phrase_list = []
        while choices:
            phrase_list.append(phrase.Phrase(choices.pop(0)))
        if settings.debug:
            print(f"\ngame.create_phrases phrase_list:")
            for ea in phrase_list:
                print(f"    {ea.phrase}")
        return phrase_list

    def get_random_phrase(self, phrase_list):
        choice = random.choice(phrase_list)
        if settings.debug:
            print(f"\ngame.get_random_phrase: {choice.phrase}")
        return choice

    def welcome(self):
        print(settings.greeting)

    def start(self):
        self.welcome()
        while self.missed < 5 and not self.active_phrase.check_complete(self.guesses):
            print(f"Number Missed: {self.missed}")
            self.active_phrase.display_guesses(self.guesses)
            self.active_phrase.display(self.guesses)
            guess = self.get_guess()
            if not self.active_phrase.check_guess(guess):
                self.missed += 1
            print("\n"*3)
        self.game_over()
        return self.play_again()


    def get_guess(self):
        print("\n")
        user_guess = self.force_letter("Your Guess?  ")
        self.guesses.append(user_guess)
        if settings.debug:
            print(f"user_guess: {user_guess}")
            print(f"self.guesses = {self.guesses}")
        return user_guess

    def game_over(self):
        print("\n"*3)
        if self.missed == 5:
            print(f"------- Game Over -------\nSorry, you had {self.missed} wrong guesses...")
        else:
            print(f"Congrats! You win!")

    def force_letter(self, prompt):
        while True:
            try:
                choice = str(input(prompt))
                full_alphabet = list(string.ascii_lowercase) + list(string.ascii_uppercase)
                if settings.DIFFICULTY == 0:
                    if choice in list(string.ascii_lowercase):
                        break
                if choice in full_alphabet:
                    break
            except:
                print(f"ERROR: Please choose one Letter between A and Z")
        return choice

    def force_int(self, prompt, min_int, max_int):
        while True:
            try:
                choice = int(input(prompt))
                if choice <= max_int:
                    break
            except:
                print(f"ERROR: Please choice an integer between {min_int} and {max_int}")
        return choice

    def play_again(self):
        print(f"\nWould you like to play again? 1 for Yes, or 2 for No")
        choice = self.force_int("choice: ", 1, 2)
        if choice == 1:
            return True
        else:
            return False


