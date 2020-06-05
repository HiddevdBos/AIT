# Hangman Game and Epistemic Logic

This repository was created in order to work for an assignment in the Logical Aspects of Multi-agent Systems course provided by the University of Groningen. 

## Hangman game
The code uses two agents, a Host and a Guesser. The Host chooses a word and updates the game after every guess, made by the Guesser. The Guesser makes guesses based on logic. We decided the usage of a hangman consisted of nine pieces which indicates that the Guesser is limited to the maximum of nine mistakes. In case that our Guesser provides nine letters that don’t exist in our Host’s word, then nine lines will be added in the hangman and the game will be terminated. 

## Setup
python 3.0 v.


To run the game, run python3 hangman.py.
