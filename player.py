from nltk.corpus import words
import random

class Player:
	
	def __init__(self, name):
		self.__result = ''  					# word to be found
		self.knowledge_opponent = []  # (part of) answer
		self.previous_guesses = []    # guesses made
		self.knowledge = []     # (part of) answer
		self.__possible = []	 				# all possible answers
		self.current_guess = ''				# current letter guessed
		self.__name = name 						# name of the player

	#choose the word the other player has to guess
	def chooseWord(self, length):
		if length == 0:
			self.__result = random.choice(words.words()).lower()	# choose random word
		else:
			while len(self.__result) != length:										# make sure opponent chooses word of same length
				self.__result = random.choice(words.words()).lower()	# choose random word
		self.knowledge_opponent = ['.'] * len(self.__result)		# information known by player


	#return the result
	def result(self):
		return self.__result

	# update knowledge of the oppontent
	def updateAnswer(self, guess):
		for idx, item in enumerate(self.__result):		#  update answer
			if item == guess:
				self.knowledge_opponent[idx] = guess

	# guess word of other player (when certain)
	def guessAnswer(self):
		return self.__possible[0]

	# select all possible worlds, based on the length of the word
	def wordLength(self):
		for word in words.words():						
			if len(word) == len(self.knowledge):
				self.__possible.append(word.lower())

	# make the guess that reduces the amount of possible worlds the most
	def guess(self):
		count = dict()														# count of all letters 
		for word in self.__possible:
			current_word_count = dict()		# count a letter only once per world
			for letter in word:
				if letter in count:
					if letter not in current_word_count:
						count[letter] += 1									
						current_word_count[letter] = 1					
				elif letter not in self.previous_guesses:
					count[letter] = 1
		self.current_guess = max(count, key=count.get)		# guess the letter that occurs most often
		self.previous_guesses.append(self.current_guess)

	# process guess of other player
	def processGuess(self, guess):
		self.current_guess = guess
		self.previous_guesses.append(guess)


	# determine which worlds are still possible
	def remaining(self):
		store___possible = self.__possible.copy()
		self.__possible.clear()
		for word in store___possible:				# for all __possible worlds
			for i, letter in enumerate(word):							# for every letter in the word
				# if the word contains a letter which has been guessed an is not at that position
				if self.knowledge[i] != '.' and self.knowledge[i] != letter:
					break
				# if word contains a letter which has already been guessed and shown to be incorrect
				if letter in self.previous_guesses and self.knowledge[i] == '.' :
					break
				if i == (len(word) - 1):
					self.__possible.append(word)

	# process announcement of other player
	def getAnswer(self, updated_answer):
		self.knowledge.clear()
		self.knowledge = updated_answer.copy()

	# return current guessed letter
	def currentGuess(self):
		return self.current_guess

	# return amount of possible worlds left
	def possibilities(self):
		return len(self.__possible)

	# return list of all possible worlds left
	def possible(self):
		return self.__possible

  # tell other player which guessed letters are at which positions
	def giveAnswer(self):
		return self.knowledge_opponent

	# return name
	def name(self):
		return self.__name
