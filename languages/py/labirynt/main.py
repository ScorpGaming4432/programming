## pre-wszystko
# importy
import random
import time
from colorama import init, deinit, Fore

# zmienne
seed = input('seed: ') # jesli chcesz losowe to puste
if seed == '': seed = None

wallcell = 1
cell = 0
pathcell = '*'
unvisited = 'u'

height = int(input('height: '))
width = int(input('width: '))
maze = []

## funkcje
# lazy ass nie chce nawet kilku for-ow napisac
def printmaze(maze):
	init()
	for i in range(len(maze)):
		for j in range(len(maze[i])):
			if maze[i][j] == wallcell: print(Fore.RED, end='')
			elif maze[i][j] == cell: print(Fore.GREEN, end='')
			elif maze[i][j] == pathcell: print(Fore.YELLOW, end='')
			print(maze[i][j], end=Fore.RESET + ' ')
		print()
	deinit()
	

# ile naokolo jest
def surroundingCells(rand_wall):
	s_cells = 0
	if (maze[rand_wall[0]-1][rand_wall[1]] == cell):
		s_cells += 1
	if (maze[rand_wall[0]+1][rand_wall[1]] == cell):
		s_cells += 1
	if (maze[rand_wall[0]][rand_wall[1]-1] == cell):
		s_cells +=1
	if (maze[rand_wall[0]][rand_wall[1]+1] == cell):
		s_cells += 1

	return s_cells


## wszystko inne
random.seed(seed)
# wszystko jako nieodwiedzone
for i in range(0, height):
	line = []
	for j in range(0, width):
		line.append(unvisited)
	maze.append(line)

# losowy początek
starting_height = int(random.random()*height)
starting_width = int(random.random()*width)
if starting_height == 0:
	starting_height += 1
if starting_height == height-1:
	starting_height -= 1
if starting_width == 0:
	starting_width += 1
if starting_width == width-1:
	starting_width -= 1

# oznacz jako wolne miejsce i dodaj ściany do listy
maze[starting_height][starting_width] = cell
walls = []
walls.append([starting_height - 1, starting_width])
walls.append([starting_height, starting_width - 1])
walls.append([starting_height, starting_width + 1])
walls.append([starting_height + 1, starting_width])

# zrob sciany wszedzie
maze[starting_height-1][starting_width] = wallcell
maze[starting_height][starting_width - 1] = wallcell
maze[starting_height][starting_width + 1] = wallcell
maze[starting_height + 1][starting_width] = wallcell

while walls:
	# wybierz losowa sciane
	rand_wall = walls[int(random.random()*len(walls))-1]

	# jesli to lewa sciana
	if (rand_wall[1] != 0):
		if (maze[rand_wall[0]][rand_wall[1]-1] == unvisited and maze[rand_wall[0]][rand_wall[1]+1] == cell):
			# przywolaj tego defa
			s_cells = surroundingCells(rand_wall)

			if (s_cells < 2):
				# okresl nowa droge
				maze[rand_wall[0]][rand_wall[1]] = cell

				# oznacz komorki
				# gora
				if (rand_wall[0] != 0):
					if (maze[rand_wall[0]-1][rand_wall[1]] != cell):
						maze[rand_wall[0]-1][rand_wall[1]] = wallcell
					if ([rand_wall[0]-1, rand_wall[1]] not in walls):
						walls.append([rand_wall[0]-1, rand_wall[1]])


				# dol
				if (rand_wall[0] != height-1):
					if (maze[rand_wall[0]+1][rand_wall[1]] != cell):
						maze[rand_wall[0]+1][rand_wall[1]] = wallcell
					if ([rand_wall[0]+1, rand_wall[1]] not in walls):
						walls.append([rand_wall[0]+1, rand_wall[1]])

				# lewa
				if (rand_wall[1] != 0):	
					if (maze[rand_wall[0]][rand_wall[1]-1] != cell):
						maze[rand_wall[0]][rand_wall[1]-1] = wallcell
					if ([rand_wall[0], rand_wall[1]-1] not in walls):
						walls.append([rand_wall[0], rand_wall[1]-1])
			

			# usun sciane
			for wall in walls:
				if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
					walls.remove(wall)

			continue

	# jesli gorna sciana
	if (rand_wall[0] != 0):
		if (maze[rand_wall[0]-1][rand_wall[1]] == unvisited and maze[rand_wall[0]+1][rand_wall[1]] == cell):

			s_cells = surroundingCells(rand_wall)
			if (s_cells < 2):
				# okresl droge
				maze[rand_wall[0]][rand_wall[1]] = cell

				# nowe sciany
				# gora
				if (rand_wall[0] != 0):
					if (maze[rand_wall[0]-1][rand_wall[1]] != cell):
						maze[rand_wall[0]-1][rand_wall[1]] = wallcell
					if ([rand_wall[0]-1, rand_wall[1]] not in walls):
						walls.append([rand_wall[0]-1, rand_wall[1]])

				# lewa
				if (rand_wall[1] != 0):
					if (maze[rand_wall[0]][rand_wall[1]-1] != cell):
						maze[rand_wall[0]][rand_wall[1]-1] = wallcell
					if ([rand_wall[0], rand_wall[1]-1] not in walls):
						walls.append([rand_wall[0], rand_wall[1]-1])

				# prawa
				if (rand_wall[1] != width-1):
					if (maze[rand_wall[0]][rand_wall[1]+1] != cell):
						maze[rand_wall[0]][rand_wall[1]+1] = wallcell
					if ([rand_wall[0], rand_wall[1]+1] not in walls):
						walls.append([rand_wall[0], rand_wall[1]+1])

			# usun
			for wall in walls:
				if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
					walls.remove(wall)

			continue

	# jesli dolna sciana
	if (rand_wall[0] != height-1):
		if (maze[rand_wall[0]+1][rand_wall[1]] == unvisited and maze[rand_wall[0]-1][rand_wall[1]] == cell):

			s_cells = surroundingCells(rand_wall)
			if (s_cells < 2):
				# nowa droga
				maze[rand_wall[0]][rand_wall[1]] = cell

				# oznacz sciany
				if (rand_wall[0] != height-1):
					if (maze[rand_wall[0]+1][rand_wall[1]] != cell):
						maze[rand_wall[0]+1][rand_wall[1]] = wallcell
					if ([rand_wall[0]+1, rand_wall[1]] not in walls):
						walls.append([rand_wall[0]+1, rand_wall[1]])
				if (rand_wall[1] != 0):
					if (maze[rand_wall[0]][rand_wall[1]-1] != cell):
						maze[rand_wall[0]][rand_wall[1]-1] = wallcell
					if ([rand_wall[0], rand_wall[1]-1] not in walls):
						walls.append([rand_wall[0], rand_wall[1]-1])
				if (rand_wall[1] != width-1):
					if (maze[rand_wall[0]][rand_wall[1]+1] != cell):
						maze[rand_wall[0]][rand_wall[1]+1] = wallcell
					if ([rand_wall[0], rand_wall[1]+1] not in walls):
						walls.append([rand_wall[0], rand_wall[1]+1])

			# usun
			for wall in walls:
				if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
					walls.remove(wall)
			continue

	# prawa
	if (rand_wall[1] != width-1):
		if (maze[rand_wall[0]][rand_wall[1]+1] == unvisited and maze[rand_wall[0]][rand_wall[1]-1] == cell):

			s_cells = surroundingCells(rand_wall)
			if (s_cells < 2):
				# nowa droga
				maze[rand_wall[0]][rand_wall[1]] = cell

				# oznacz sciany
				if (rand_wall[1] != width-1):
					if (maze[rand_wall[0]][rand_wall[1]+1] != cell):
						maze[rand_wall[0]][rand_wall[1]+1] = wallcell
					if ([rand_wall[0], rand_wall[1]+1] not in walls):
						walls.append([rand_wall[0], rand_wall[1]+1])
				if (rand_wall[0] != height-1):
					if (maze[rand_wall[0]+1][rand_wall[1]] != cell):
						maze[rand_wall[0]+1][rand_wall[1]] = wallcell
					if ([rand_wall[0]+1, rand_wall[1]] not in walls):
						walls.append([rand_wall[0]+1, rand_wall[1]])
				if (rand_wall[0] != 0):	
					if (maze[rand_wall[0]-1][rand_wall[1]] != cell):
						maze[rand_wall[0]-1][rand_wall[1]] = wallcell
					if ([rand_wall[0]-1, rand_wall[1]] not in walls):
						walls.append([rand_wall[0]-1, rand_wall[1]])

			# usun
			for wall in walls:
				if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
					walls.remove(wall)
			continue

	# jesli if nie ifuje to wywal
	for wall in walls:
		if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
			walls.remove(wall)
	


# nieodwiedzone to sciany
for i in range(0, height):
	for j in range(0, width):
		if (maze[i][j] == unvisited):
			maze[i][j] = wallcell

# poczatek i koniec
for i in range(0, width):
	if (maze[1][i] == cell):
		maze[0][i] = 'P'
		break

for i in range(width-1, 0, -1):
	if (maze[height-2][i] == cell):
		maze[height-1][i] = 'K'
		break

# wyprintuj
#maze = [['x', 'P', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], ['x', '.', 'x', '.', '.', '.', '.', 'x', '.', 'x'], ['x', '.', 'x', 'x', 'x', 'x', '.', '.', '.', 'x'], ['x', '.', 'x', '.', 'x', 'x', 'x', 'x', '.', 'x'], ['x', '.', '.', '.', '.', 'x', '.', 'x', '.', 'x'], ['x', 'x', 'x', 'x', '.', 'x', '.', 'x', '.', 'x'], ['x', '.', '.', 'x', '.', 'x', '.', 'x', '.', 'x'], ['x', 'x', '.', 'x', '.', 'x', '.', 'x', '.', 'x'], ['x', '.', '.', '.', '.', '.', '.', '.', '.', 'x'], ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'K', 'x']]
printmaze(maze)


## nawarzyles to teraz pij
from collections import deque

def bidirectional_search(maze, start, end):
	rows, cols = len(maze), len(maze[0])
	directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

	# Initialize search frontiers from both start and end points
	start_queue = deque([(start, [])])
	end_queue = deque([(end, [])])

	# Track visited nodes and paths from both directions
	start_visited = {start: []}
	end_visited = {end: []}

	while start_queue and end_queue:
	    # Expand search from the start point
		current, path = start_queue.popleft()
		if current in end_visited:  # Meeting point found
			return path + [current] + end_visited[current][::-1]

		for dr, dc in directions:
			r, c = current[0] + dr, current[1] + dc
			if 0 <= r < rows and 0 <= c < cols and maze[r][c] == cell and (r, c) not in start_visited:
				start_queue.append(((r, c), path + [current]))
				start_visited[(r, c)] = path + [current]

	    # Expand search from the end point
		current, path = end_queue.popleft()
		if current in start_visited:  # Meeting point found
			return start_visited[current][::-1] + [current] + path

		for dr, dc in directions:
			r, c = current[0] + dr, current[1] + dc
			if 0 <= r < rows and 0 <= c < cols and maze[r][c] == cell and (r, c) not in end_visited:
				end_queue.append(((r, c), path + [current]))
				end_visited[(r, c)] = path + [current]

	return None  # No meeting point found

print(maze[-1].index('K'))
# Example usage:
start = (0, maze[0].index('P'))
end = (len(maze)-1, maze[-1].index('K'))
path = bidirectional_search(maze, start, end)
if path:
	tmpmaze = maze
	for i, j in path:
		tmpmaze[i][j] = pathcell
	print('Shortest path found:')
	for row, col in path:
		print(f'({row}, {col}) -> ', end='')
	print('End')
	printmaze(tmpmaze)
else:
	print('No path found.')
input('\nProgram Finished')