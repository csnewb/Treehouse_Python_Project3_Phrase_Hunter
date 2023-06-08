# Create your Phrase class logic here.

class Phrase():
    def __init__(self, phrase: str):
        self.phrase = phrase.lower()

    def display(self, guesses):
        output = ""
        for letter in self.phrase:
            if letter in guesses:
                output += letter
            elif letter == " ":
                output += letter
            else:
                output += "_"
            output += " "
        print(output)
        return output

    def check_guess(self, guess):
        if guess in self.phrase:
            print("Correct!")
            return True
        else:
            print("Sorry, incorrect... try again!")
            return False

    def check_complete(self, guesses):
        for letter in self.phrase:
            if letter != " ":
                if letter not in guesses:
                    return False
        return True

    def display_guesses(self, guesses):
        display_text = ", ".join(guesses)
        print(f"Guessed Letters: \n{display_text}\n")

