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

def find_best_node(opened:List[Node], goal: State) -> Node:
	if len(opened) == 1:
		return opened[0]
	best_node = opened[0]
	cost = find_cost(best_node, goal)
	for i in range(1, len(opened) - 1):
		tmp = find_cost(opened[i], goal)
		if cost > tmp:
			cost = tmp;
			state = opened[i]
	return best_node


def is_in_list(a_list: List[Node], target: List[List[int]]) -> Node | None:
	for index, el in enumerate(a_list):
		if el.state.matrix == target:
			return el
	return None

def a_star(puzzle):
	goal = solution_puzzle(puzzle)

	root = Node(prev=None, state=State(g=0, matrix=puzzle))

	opened = [root]
	closed = []

	while is_in_list(opened, goal) is None:
		current = find_best_node(opened, goal)
		opened.remove(current)
		closed.append(current)
		print('Bye')
		new_states = current.state.generate_new_states(get_idx(current.state, 0))
		
		for state in new_states:
			print('Hi')
			open_ist = is_in_list(opened, state.matrix)
			close_ist = is_in_list(closed, state.matrix)
			if open_ist is not None and open_ist.state.g > state.g:
				open_ist.change_path(state.g, current)
			elif close_ist is not None and close_ist.state.g > state.g:
				close_ist.change_path(state.g, current)
			else:
				child_node = Node(prev=current, state=state)
				opened.append(child_node)
		
	return 0

def main():
	puzzle = [
		[6, 1, 8], 
		[2, 5, 4],
		[7, 3, 0]
		]

	a_star(puzzle)
	print('hey')

if __name__ == '__main__':
    main()