
# Wordle Bot

A Bot written in python with a CL 
Interface to guess adn solve Wordle Puzzles
efficiently. 




## Usage/Examples

```python

from process import WordleGuessBot

def main():
    wbot = WordleGuessBot()
    """
        If you know the answer you 
        can initialize the object with argument
        gs = WordleGuessBot("amber")
    """
    wbot.guess_process()

if __name__ == "__main__":
    main()

# GUESS : amber

```


```txt
WORDLE ANSWER : "AMBER"

> Open the command line and execute main.py
    

    =>  Bot makes an opener guess 
    >> ATTEMPT MADE : SENOR


    =>  You input the guess in the wordle interface and 
        then remove unwanted chars by typing them together 
        in a string 
    >> REMOVE CHARS : sno

    =>  Similary type all the chars in a string 
        that were yellow or green. 
    >> ADD CHARS : er

    =>  Finally if some characters were green use 0-based indexing
        to indicate their position, if some characters were 
        yellow use '*' to indicate the bot that the 
        character's postion is unknown as of now.
        **************************************************
        (Note :  Type the indices or '*' in the exact same order as
        you entered in "ADD CHARS : " prompt, For example in the
        above example "er" relates to "*4" as if postion
        of "e" is unknows and "r" is at the 4th index of the word)
        **************************************************
    >> INDICES OF INCLUDED CHARS : *4

    REPEAT UNTIL THE BOT GUESSES THE CORRECT ANSWER

```


## Features

- Usually guesses b/w 3-4 turns
- Guessing pattern based on the Entropy Function in Information Theory
- User Freidnly CLI

## Requirements

- Numpy
- Pandas