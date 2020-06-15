from player import *

# start of the game, player chooses a word and 
def startGame(player_1, player_2):
	player_1.chooseWord(len(player_2.result()))	# choose a random word
	player_2.getAnswer(player_1.giveAnswer())	# tell player_1 how many letters the word is
	player_2.wordLength()	# process word length 

	print(player_1.name(), "chooses the word", player_1.result())

def playRound(player_1, player_2):
	player_1.guess()	# guess a letter

	print(player_1.name(), "guesses", player_1.currentGuess(), '\n')

	player_2.processGuess(player_1.currentGuess())
	player_1.updateAnswer(player_2.currentGuess()) # show whether letter is present
	player_2.updateAnswer(player_1.currentGuess()) # show whether letter is present
	player_1.getAnswer(player_2.giveAnswer())	# process other player's reaction
	player_2.getAnswer(player_1.giveAnswer())	# process other player's reaction
	player_1.remaining()
	player_2.remaining()

	print (player_1.name(), 'current knowledge is',''.join(player_2.giveAnswer()))			 # print letters of word known by player_1
	print (player_1.name(), "has", player_1.possibilities(), "possible worlds remaining")
	if (player_1.possibilities() < 10):
		print (player_1.name(), "remaining worlds are:", ', '.join(player_1.possible()))
	print ('')
	print (player_2.name(), 'current knowledge is',''.join(player_1.giveAnswer()))			 # print letters of word known by player_1
	print (player_2.name(), "has", player_2.possibilities(), "possible worlds remaining")
	if (player_2.possibilities() < 10):
		print (player_2.name(), "remaining worlds are:", ', '.join(player_2.possible()))
	print ('')

# initialize 2 players
player_1 = Player('player 1')		# player_1 trying to guess the word
player_2 = Player('player 2') 	# player_2 of the game

# prepare the game
startGame(player_1, player_2)
startGame(player_2, player_1)
input("\npress any key to start the game\n")

# play the game. Continues until one of the players guesses the word of the other player
while True:
	if player_1.possibilities() == 1:	# if player_1 knows player_2's word
		print (player_1.name(), "guesses", player_1.guessAnswer())
		print (player_1.name(), "wins")
		break # exit loop, ending game
	
	playRound(player_1, player_2)
	input("press any key to go to the next round\n")
	
	if player_2.possibilities() == 1: # if player_2 knows player_1's word
		print (player_2.name(), "guesses", player_2.guessAnswer())
		print (player_2.name(), "wins")	
		break # exit loop, ending game
	
	playRound(player_2, player_1)
	input("press any key to go to the next round\n")