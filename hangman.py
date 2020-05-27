from host import *
from player import *

player = Player()	# player trying to guess the word
host = Host() 		# host of the game

host.chooseWord()	# choose a random word
player.getAnswer(host.getAnswer())	# tell player how many letters the word is
player.wordLength()	# process word length 

while player.notFinished() and host.incorrectGuesses() < 8:
	player.guess()	# guess a letter
	host.updateAnswer(player.currentGuess()) # show whether letter is present
	player.getAnswer(host.getAnswer())	# process hosts reaction
	player.remaining()

	print(player.currentGuess()) # print guess of the player
	print(host.getAnswer())			 # print letters of word known by player
	print(player.possibilities())
	print(host.incorrectGuesses())
	print('\n')
