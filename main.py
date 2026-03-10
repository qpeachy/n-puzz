from typing import List, Dict, Tuple

def solution_puzzle(puzzle: List[List[int]]) -> List[List[int]]:
	#TODO:do this shit
	return [
		[1, 2, 3],
		[8, 0, 4],
		[7, 6, 5]]

def get_idx(current: List[List[int]], target: int) -> Tuple:
	for i, row in enumerate(current):
		for j, value in enumerate(row):
			if value == target:
				return (i, j)
	return (-1, -1)


def find_cost(current: List[List[int]], goal: List[List[int]]) -> int:
	cost = 0
	l = len(current)
	for i in range(l * l - 1):
		a = get_idx(current, i)
		b = get_idx(goal, i)
		cost += abs(a[0] - b[0]) + abs(a[1] - b[1])	
	return cost

def find_best_state(open_states: List[Dict], goal: List[List[int]]) -> Dict:
	if len(open_states) == 1:
		return open_states[0]
	state = open_states[0]
	cost = find_cost(open_states[0]["puzzle"], goal)
	for i in range(1, len(open_states) - 1):
		tmp = find_cost(open_states[i]["puzzle"], goal)
		if cost > tmp:
			cost = tmp;
			state = open_states[i]
	return state

def switch(current: List[List[int]], zero_idx: Tuple, switch_idx: Tuple[int, int]) -> List[List[int]]:
	current[zero_idx[0]][zero_idx[1]] = current[switch_idx[0]][switch_idx[1]]
	current[switch_idx[0]][switch_idx[1]] = 0
	return current

def generate_new_states(current:List[List[int]], zero_idx: Tuple[int,int]) -> List[List[int]]:
	#look for [+1][] [-1][] [][+1] [][-1]
	new_states = []
	if zero_idx[0] + 1 > len(current):
		new_states.append(switch(current, zero_idx, switch_idx = (zero_idx[0] + 1, zero_idx[1])))
	if zero_idx[0] - 1 > -1:
		new_states.append(switch(current, zero_idx, switch_idx = (zero_idx[0] - 1, zero_idx[1])))
	if zero_idx[1] + 1 < len(current):
		new_states.append(switch(current, zero_idx, switch_idx = (zero_idx[0], zero_idx[1] + 1)))
	if zero_idx[1] - 1 > -1:
		new_states.append(switch(current, zero_idx, switch_idx = (zero_idx[0], zero_idx[1] - 1)))
	return new_states

def a_star(puzzle):
	goal = solution_puzzle(puzzle)
	state = {"puzzle": puzzle, "path": []}
	opened = [state]
	closed = []
	while puzzle is not goal :
		current = find_best_state(opened, goal)
		opened.extend(generate_new_states(current, get_idx(current, 0)))
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