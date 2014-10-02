'''
Usage:
	racesolver.py <map-file>
	racesolver.py -d <maximum-depth> <map-file>

Options:	
	-d <max-depth>	Change maximum depth. Default: 30. Higher values
					make it more likely that the solver finds a sol-
					ution, but will increase runtime.
'''


import sys
import docopt

from geometry import *
from collections import Counter
from time import sleep

options = docopt.docopt(__doc__, version="Racetrack-Solver 1.1.0")

def moves(car,board):
	'''Returns all possible legal moves for a given car'''
	for x in range(-1,2,1):
		for y in range(-1,2,1):
			new = (car[0] + x + car[2], car[1] + y + car[3], car[2] + x, car[3] + y)
			line = ((car[0],car[1]),(new[0],new[1]))
			if any([line_intersection(line,edge) for edge in board]):
				continue
			if line_intersection(line, goal_helper):
				if not (line_intersection(line, goal) and distance(car,middle_point(goal)) < distance(car,middle_point(goal_helper))):
					continue
			yield new

i = __import__(options['<map-file>'][:-3], globals(), locals(), ['car', 'goal', 'goal_helper', 'board'])

car = i.car
goal = i.goal
goal_helper = i.goal_helper
board = i.board

evaluation_function = linedistance

seen = Counter()
shortest = ":)"*15

if options['-d']:
	shortest = "." * (int(options['<maximum-depth>'])+1)

def turn(car,history):
	global shortest
	global seen
	if car in seen and seen[car] <= len(history):
		return
	else:
		seen[car] = len(history)
	if len(history)+1 >= len(shortest):
		return
	for move in sorted(moves(car,board),key=lambda x: evaluation_function(x,goal)):
		if line_intersection((car,move), goal):
			if len(shortest) > len(history)+2:
				shortest = history + [car] + [move]
				print("Found route of length ",len(shortest))
		else:
			turn(move,history + [car])
	return shortest

print("Car:",car)
print("Goal:",goal)
print("Board:",board)
print("Reticulating splines...")
print(turn(car,[]))