from typing import List, Tuple, Optional
import copy

class State:
	def __init__(self, g:int, matrix:List[List[int]]):
		self.g = g
		self.matrix = matrix

	@staticmethod
	def swap(state: 'State', zero_idx: Tuple, swap_idx: Tuple[int, int]) -> 'State':
		new_matrix = copy.deepcopy(state.matrix)
		state.matrix[zero_idx[0]][zero_idx[1]] = state.matrix[swap_idx[0]][swap_idx[1]]
		state.matrix[swap_idx[0]][swap_idx[1]] = 0
		return State(g=state.g + 1, matrix=new_matrix)

	def generate_new_state(self, zero_idx: Tuple[int,int]) -> List['State']:
		new_states: List['State'] = []
		if zero_idx[0] + 1 > len(self.matrix):
			swap_idx = (zero_idx[0] + 1, zero_idx[1])
			new_states.append(self.swap(self, zero_idx, swap_idx))
		if zero_idx[0] - 1 > -1:
			swap_idx = (zero_idx[0] - 1, zero_idx[1])
			new_states.append(self.swap(self, zero_idx, swap_idx))
		if zero_idx[1] + 1 < len(self.matrix):
			swap_idx = (zero_idx[0], zero_idx[1] + 1)
			new_states.append(self.swap(self, zero_idx, swap_idx))
		if zero_idx[1] - 1 > -1:
			swap_idx = (zero_idx[0], zero_idx[1] - 1)
			new_states.append(self.swap(self, zero_idx, swap_idx))
		return new_states

""" 
get h (current to goal)
generate new states from state
swap
"""

#liste chaine ou il y a un state (remplacer la current)
class Node:
	def __init__(self, prev: Optional['Node'], state: 'State'):
		self.state = state
		self.prev = prev
		self.g = prev.state.g + 1 if prev is not None else 0

""" 
fonctions de listes chainees
get f
"""
