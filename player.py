from nltk.corpus import words

class Player:
	
	def __init__(self):
		self.previous_guesses = []    # guesses made
		self.answer = []     # (part of) answer
		self.possible = []	 # all possible answers
		self.current_guess = ''


	def wordLength(self):
		for word in words.words():								
			if len(word) == len(self.answer):						
				self.possible.append(word.lower())

	def guess(self):
		counts = dict()														# count of all letters 
		for word in self.possible:
			for letter in word:
				if letter in counts:
					counts[letter] += 1
				elif letter not in self.previous_guesses:
					counts[letter] = 1
		self.current_guess = max(counts, key=counts.get)		# guess the letter that occurs most often
		self.previous_guesses.append(self.current_guess)

	def remaining(self):
		store_possible = self.possible.copy()
		self.possible.clear()
		for word in store_possible:
			correct = 1
			count = 0
			for letter in word:
				if self.answer[count] != '.' and self.answer[count] != letter:
					correct = 0
				count += 1
			if correct == 1:
				self.possible.append(word)

	def getAnswer(self, updated_answer):
		self.answer.clear()
		self.answer = updated_answer.copy()

	def currentGuess(self):
		return self.current_guess

	def notFinished(self):
		return '.' in self.answer 

	def possibilities(self):
		return len(self.possible)