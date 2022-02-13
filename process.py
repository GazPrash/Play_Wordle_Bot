# For Filtering & Guessing Words
import pandas as pd
import random as rd
from guesser import entropy_function


class WordleGuessBot:
    def __init__(self) -> None:
        # loading_data
        self.available_words = pd.read_csv("main_data/Allowed_Words.csv")
        self.available_words = self.available_words["0"].to_list()
        self.freqs = pd.read_csv("main_data/Word_Usage_Frequency.csv")
        self.freqs.sort_values(by = 'Prob', ascending = False, inplace = True)
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
                remove_chars.append(char)

            for char2 in input("ADD CHARS : "):
                append_chars.append(char2)
            
            for char3 in input("INDICES OF INCLUDED CHARS : "):
                if char3 == "*":
                    append_sel_indices.append(-1)
                    continue
                append_sel_indices.append(int(char3))

            if refactored_list != []:
                self.available_words = list(set(refactored_list).intersection(self.available_words))
                refactored_list = []

            print(remove_chars)
            print()
            print(append_chars)

            for word in self.available_words:
                if set(remove_chars).intersection(word) == set() and set(append_chars).intersection(word) != set():
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

                print(self.recieved_guesses)
                print("\n ** NOW MAKING A GUESS ** \n")

                print(f"RECOMMENDED GUESS : {self.recieved_guesses[0]}")

            i += 1
            prompt = input("Press Enter to Conitune or 'X' to Exit the Program >> ")
