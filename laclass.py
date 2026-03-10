class State:
	def __init__(self, g, matrix):
		self.g = g
		self.matrix = matrix

""" 
get h (cureent to goal)
generate new states from state
switch
"""



class Node:
	def __init__(self, prev, state):
		self.prev = prev
		self.g = prev.g + 1 if prev is not None else 0
		self.next = None
		self.state = state

""" 
fonctions de listes chainees
get f
"""
