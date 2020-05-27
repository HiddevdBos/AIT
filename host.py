from nltk.corpus import words
import random

class Host:

	def __init__(self):
		self.result = ''   					  # word to be found
		self.answer = []     					# (part of) answer
		self.incorrect_guesses = 0	 # number of incorrect guesses

	def chooseWord(self):
		self.result = random.choice(words.words()).lower()	# choose random word
		self.answer = ['.'] * len(self.result)						# information known by player

	def updateAnswer(self, guess):
		correct = 0
		for idx, item in enumerate(self.result):		#  update answer
			if item == guess:
				correct = 1
				self.answer[idx] = guess
		if correct == 0:
			self.incorrect_guesses +=1

	def incorrectGuesses(self):
		return self.incorrect_guesses

	def getAnswer(self):
		return self.answer

