## Downloading and Aggergating required datasets
import pandas as pd
import requests
from numpy import arange as nrange

def guessable_words_total():
    dt_response = requests.get("https://www-cs-faculty.stanford.edu/~knuth/sgb-words.txt")
    words_list = dt_response.text.split()
    data = pd.Series(words_list, index = nrange(0, len(words_list)))
    data.to_csv("Data/Allowed_Words.csv")


def google_ngram_word_freq():
    words = []
    data = []

    with open("data/long_freqs.txt", "r") as file:
        for line in file.readlines():
            word, fq = line.split()
            try:
                words.append(word)
                data.append(float(fq))
            except Exception as e:
                print(e)        

    with open("data/short_freqs.txt", "r") as file:
        for line in file.readlines():
            word, fq = line.split()
            try:
                words.append(word)
                data.append(float(fq))
            except Exception as e:
                print(e) 

    word_freq = pd.DataFrame()
    word_freq["Word"] = words
    word_freq["Freq"] = data
    word_freq["Prob"] = [100 * x for x in data]
    word_freq.index = nrange(1, len(data)+1)

    word_freq.to_csv("Data/Word_Usage_Frequency.csv")


def main():
    guessable_words_total()
    google_ngram_word_freq()


if __name__ == "__main__":
    main()