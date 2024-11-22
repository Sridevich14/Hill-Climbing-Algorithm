import numpy as np 
 
 
class Puzzle8HillClimbing: 
def  init (self, initial_state, goal_state): 
self.initial_state = initial_state 
self.goal_state = goal_state 
self.goal_positions = {value: (i, j) for i, row in enumerate(goal_state) for j, value in 
enumerate(row)} 
self.visited_states = set() 
def heuristic(self, state): 
"""Calculate the Manhattan distance heuristic.""" 
distance = 0 
for i in range(3): 
for j in range(3): 
value = state[i][j] 
if value != 0: # Skip the blank tile 
goal_i, goal_j = self.goal_positions[value] 
distance += abs(i - goal_i) + abs(j - goal_j) 
return distance 
 
 
def find_blank_tile(self, state): 
"""Find the position of the blank tile (0).""" 
for i, row in enumerate(state): 
for j, value in enumerate(row): 
if value == 0: 
return i, j 
 
 
def get_neighbors(self, state): 
"""Generate all possible neighbors by moving the blank tile.""" 
neighbors = [] 
x, y = self.find_blank_tile(state) 
moves = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)] # Up, Down, Left, Right 
 
 
for new_x, new_y in moves: 
if 0 <= new_x < 3 and 0 <= new_y < 3: 
new_state = [list(row) for row in state] 
# Swap blank tile with adjacent tile 
new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y] 
neighbors.append(new_state) 
 
 
return neighbors 
 
 
def hill_climbing(self): 
"""Hill Climbing algorithm to solve the 8 Puzzle.""" 
current_state = self.initial_state 
current_heuristic = self.heuristic(current_state) 
 
 
steps = [current_state] 
self.visited_states.add(tuple(map(tuple, current_state))) 
 
while current_heuristic > 0: 
neighbors = self.get_neighbors(current_state) 
best_neighbor = None 
best_heuristic = float('inf') 
 
 
for neighbor in neighbors: 
neighbor_tuple = tuple(map(tuple, neighbor)) 
if neighbor_tuple in self.visited_states: 
continue 
 
 
h = self.heuristic(neighbor) 
if h < best_heuristic: 
best_neighbor = neighbor 
best_heuristic = h 
 
if best_heuristic >= current_heuristic: 
print("Stuck at a local maximum or plateau.") 
break 
 
 
current_state = best_neighbor 
current_heuristic = best_heuristic 
steps.append(current_state) 
self.visited_states.add(tuple(map(tuple, current_state))) 
 
 
return steps 
 
 
def print_state(self, state): 
"""Print the puzzle state.""" 
for row in state: 
print(" ".join(map(str, row))) 
print() 
 
# Define multiple test cases 
test_cases = [ 
{ 
"description": "Success Case: Easy solvable", 
"initial_state": [ 
[1, 2, 3], 
[4, 0, 5], 
[7, 8, 6] 
] 
}, 
{ 
"description": "Success Case: Moderate solvable", 
"initial_state": [ 
[1, 2, 3], 
[4, 8, 0], 
[7, 6, 5] 
] 
}, 
{ 
"description": "Failure Case: Local maxima", 
"initial_state": [ 
[1, 2, 3], 
[4, 6, 0], 
[7, 5, 8] 
] 
}, 
{ 
"description": "Failure Case: Plateau", 
"initial_state": [ 
[1, 2, 3], 
[0, 4, 5], 
[7, 8, 6] 
] 
}, 
{ 
"description": "Failure Case: Unsolvable configuration", 
"initial_state": [ 
[1, 2, 3], 
[4, 5, 6], 
[8, 7, 0] 
] 
} 
] 
# Goal state 
goal_state = [ 
[1, 2, 3], 
[4, 5, 6], 
[7, 8, 0] 
] 
 
 
# Run each test case 
for idx, test_case in enumerate(test_cases, 1): 
print(f"\n=== Test Case {idx}: {test_case['description']} ===") 
initial_state = test_case["initial_state"] 
puzzle_solver = Puzzle8HillClimbing(initial_state, goal_state) 
steps = puzzle_solver.hill_climbing() 
 
print("\nInitial State:") 
puzzle_solver.print_state(initial_state) 
 
if steps: 
print("\nSolution Steps:") 
for i, step in enumerate(steps): 
print(f"Step {i + 1}:") 
puzzle_solver.print_state(step) 
else: 
print("No solution found.") 
 
 
if len(steps) == 1: 
print("\nAnalysis of Failure:") 
print("- The algorithm failed to make progress.") 
print("- Likely causes: local maxima, plateau, or unsolvable configuration.") 
else: 
print("\nFinal Analysis:") 
print("- The Hill Climbing algorithm successfully solved the problem.") 
print("- However, it may fail in more challenging cases.") 
 
print("\nAll test cases completed.") 
