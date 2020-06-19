# Hangman Game and Epistemic Logic

This repository was created in order to work for an assignment in the Logical Aspects of Multi-agent Systems course provided by the University of Groningen. 

## Hangman game
This code is a symmetric Hangman game, using two agents. The difference with the traditional hangman game is that this version is player vs player, instead of player vs host. In this version, both agents choose a word at the start of the game. At every turn, one of the players makes a guess, based on logic, and both players show whether the guessed letter is present in the word they chose. The goal of the agents is to guess the word of the opponent, before the opponent guesses their word.

## Setup
python 3.0 v.
Natural Language Toolkit (NLTK) 3.5 V.

## Running the code

The code can be run with the following command:

```
python3 hangman.py
```
In case you receive an error regarding nltk library: 

```pip3 install nltk
```

In case you receive an error regarding corpora/words run the following command and later follow the process through the window that appears:

```
python3 -c ("import nltk; nltk.dowload()")
```
