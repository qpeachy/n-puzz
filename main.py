from typing import List, Dict, Tuple
from laclass import State, Node

def solution_puzzle(puzzle: List[List[int]]) -> State:
	#TODO:do this shit
	return State(g=0, matrix=[
		[1, 2, 3],
		[8, 0, 4],
		[7, 6, 5]])

def get_idx(state: State, target: int) -> Tuple:
	for i, row in enumerate(state.matrix):
		for j, value in enumerate(row):
			if value == target:
				return (i, j)
	return (-1, -1)

def find_cost(current: Node, goal: State) -> int:
	cost = 0
	l = len(current.state.matrix)
	for i in range(l * l - 1):
		a = get_idx(current.state, i)
		b = get_idx(goal, i)
		cost += abs(a[0] - b[0]) + abs(a[1] - b[1])	
	return cost

def find_best_node(open_list:List[Node], goal: State) -> Node:
	if len(open_list) == 1:
		return open_list[0]
	best_node = open_list[0]
	cost = find_cost(best_node, goal)
	for i in range(1, len(open_list) - 1):
		tmp = find_cost(open_list[i], goal)
		if cost > tmp:
			cost = tmp;
			state = open_list[i]
	return best_node

def a_star(puzzle):
	goal = solution_puzzle(puzzle)

	start_state = State(g=0, matrix=puzzle)
	start_node = Node(prev=None, state=start_state)

	open_list = [start_node]
	close_list = []

	while open_list :
		current_node = find_best_node(open_list, goal)
		open_list.remove(current_node)
		close_list.append(current_node)

		new_states = current_node.state.generate_new_states(get_idx(0))
		
		for state in new_states:
			if open_list
			child_node = Node(prev=current_node, state=state)
			open_list.append(child_node)
	return 0

def main():
	puzzle = [
		[6, 1, 8], 
		[2, 5, 4],
		[7, 3, 0]
		]

	# opened.append(puzzle)
	# generate_possible_moves
	# opened.append(possible_moves)
	# opened.remove(puzzle)
	# closed.append(puzzle)
	# find_cheapest_move(opened)
	# puzzle = {"state" : [
	# 	[6, 1, 8], 
	# 	[2, 5, 4],
	# 	[7, 0, 3]
	# 	],
	# 	"path": [states]}
	# generate_possible_moves