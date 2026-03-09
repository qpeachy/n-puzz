from typing import List, Dict

def solution_puzzle(puzzle: List[List[int]]):
	#TODO:do this shit
	return [
		[1, 2, 3],
		[8, 0, 4],
		[7, 6, 5]]

def return_index(current: List[List[int]], target: int):
	for i, row in enumerate(current):
		for j, value in enumerate(row):
			if value == target:
				return (i, j)
	return None


def find_cost(current: List[List[int]], goal: List[List[int]]) -> int:
	cost = 0
	l = len(current)
	for i in range(l * l - 1):
		a = return_index(current, i)
		b = return_index(goal, i)
		cost += abs(a[0] - b[0]) + abs(a[1] - b[1])	
	return cost

def find_best_state(open_states: List[Dict], goal: List[List[int]]) -> List:
	if len(open_states) == 1:
		return open_states[0]
	state = open_states[0]
	cost = find_cost(open_states[0])
	for i in range(1, len(open_states) - 1):
		tmp = find_cost(open_states[i])
		if cost > tmp:
			cost = tmp;
			state = open_states[i]
	return state

def generate_new_states():

def a_star(puzzle):
	goal = solution_puzzle(puzzle)
	state = {"puzzle": puzzle, "path": []}
	opened = [state]
	closed = []
	while puzzle is not goal :
		current = find_best_state(opened, goal)
		opened.extend(generate_new_states(current))


def main():
	puzzle = [
		[6, 1, 8], 
		[2, 5, 4],
		[7, 3, 0]
		]
	puzzle = [
		[6, 1, 8], 
		[2, 5, 0],
		[7, 3, 4]
		] + 1
	puzzle = [
		[6, 1, 8], 
		[2, 5, 4],
		[7, 0, 3]
		] - 1 + 10
	opened = []
	closed = []


	opened.append(puzzle)
	# blablabla
	generate_possible_moves
	opened.append(possible_moves)
	opened.remove(puzzle)
	closed.append(puzzle)
	find_cheapest_move(opened)
	puzzle = {"state" : [
		[6, 1, 8], 
		[2, 5, 4],
		[7, 0, 3]
		],
		"path": [states]}
	generate_possible_moves