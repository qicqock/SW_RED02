class Card: 
	suits = ("Diamond", "Heart", "Spade", "Clover")
	ranks = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")    
	def __init__(self, suit, rank, face_up=True): 
		self.suit = suit 
		self.rank = rank 
		self.face_up = face_up 
	def flip(self): 
		self.face_up = not self.face_up