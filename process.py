# For Filtering & Guessing Words
import pandas as pd
import random as rd
from guess_entropy import entropy_function


class WordleGuessBot:
    def __init__(self, starter=None) -> None:
        # use this variable if you already know the answer
        self.starter = starter

        # loading_data
        self.available_words = pd.read_csv("main_data/Allowed_Words.csv")
        self.available_words = self.available_words["0"].to_list()
        self.freqs = pd.read_csv("main_data/Word_Usage_Frequency.csv")
        self.freqs.sort_values(by="Prob", ascending=False, inplace=True)
        self.recieved_guesses = {}

    def top_suggestion(self):
        if self.recieved_guesses == dict():
            return self.freqs.iloc[0]["Word"]

        return self.recieved_guesses[-1]

    def guess_process(self):
        # starting with a select group of starters.
        attempt = ""
        prompt = ""

        refactored_list = []

        starters = [
            "AROSE",
            "EARLS",
            "LASER",
            "REALS",
            "ALOES",
            "REAIS",
            "NOTES",
            "RESIN",
            "TARES",
            "SENOR",
        ]

        attempt = rd.choice(starters)
        print(f"ATTEMPT MADE : {attempt}")

        i = 0
        while prompt.upper() != "X":
            app_word = True
            append_chars = []
            remove_chars = []
            append_sel_indices = []

            for char in input("REMOVE CHARS : "):
                remove_chars.append(char.lower())

            for char2 in input("ADD CHARS : "):
                append_chars.append(char2.lower())

            for ind in input("INDICES OF INCLUDED CHARS : "):
                if ind == "*":
                    append_sel_indices.append(-1)
                    continue
                append_sel_indices.append(int(ind))

            if refactored_list != []:
                self.available_words = list(
                    set(refactored_list).intersection(self.available_words)
                )
                refactored_list = []

            for word in self.available_words:
                if (
                    set(remove_chars).intersection(word) == set()
                    and set(append_chars).intersection(word) != set()
                ):
                    for ch, ind in zip(append_chars, append_sel_indices):
                        if ind == -1:
                            if ch not in word:
                                app_word = False
                                break
                        else:
                            if word[ind] != ch:
                                app_word = False
                                break
                    if app_word:
                        refactored_list.append(word)
                    else:
                        app_word = True
            # print(refactored_list)

            if refactored_list != []:
                self.recieved_guesses = entropy_function(refactored_list, self.freqs)
                print(self.recieved_guesses[:10])
                print("\n ** NOW MAKING A GUESS ** \n")

                sec_prompt = ""
                iter = 0
                while sec_prompt.lower() != "y":
                    guess_made = self.recieved_guesses[iter]
                    print(f"RECOMMENDED GUESS : {guess_made}")
                    sec_prompt = input(
                        "Press 'Y/y' to make the guess or 'N/n' for the next guess : "
                    )
                    if sec_prompt.lower() == "n":
                        iter += 1

                if self.starter is not None:
                    if self.starter == guess_made[0]:
                        print("GUESS WAS SUCCESSFULL!")
                        return

            i += 1
            if self.starter is not None:
                prompt = input(
                    """Guess was Unsuccessful Remove or Add Characters according to the Wordle Results 
    (Note : Press Enter to continue or 'X' to Exit the Program) \n>> """
                )
            else:
                prompt = input(
                    """Continue the process ? (Press Anything) 
    (Note : Press Enter to continue or 'X' to Exit the Program) \n>> """
                )

