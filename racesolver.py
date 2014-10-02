import sys

from geometry import line_intersection
from collections import Counter
from time import sleep

# car = (21,2,0,2)
# goal = (5,22)
# board = {((0,0),(23,0)),((23,0),(23,10)),((23,10),(18,17)),((18,17),(5,17)),((5,17),(5,19)),((5,19),(9,24)),((9,24),(0,24)),((0,24),(0,0))}

# car = (17,3,-1,0)
# goal = ((2,19),(2,25))
# board = {((0,0),(18,0)),((18,0),(18,6)),((18,6),(5,6)),((5,6),(5,12)),((5,12),(7,15)),((7,15),(16,15)),((16,15),(16,25)),((16,25),(0,25)),((0,25),(0,0)),((0,19),(5,19))}

# car = (2,1,0,1)
# goal = ((4,1),(9,1))
# board = (((0,0),(4,0)),((9,0),(9,7)),((9,7),(0,7)),((0,7),(0,0)),((4,0),(4,4)))

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

def build_path(listofpoints):
	return set(zip(listofpoints[:-1],listofpoints[1:]))

def distance(pos1,pos2):
	return abs(pos1[0]-pos2[0]) + abs(pos1[1]-pos2[1])

def linedistance(pos1,line):
	pos2 = middle_point(line)
	return abs(pos1[0]-pos2[0]) + abs(pos1[1]-pos2[1])

def middle_point(line):
	return ((line[0][0]+line[1][0])/2,(line[0][1]+line[1][1])/2)
	
	
car = (4,25,0,-1)
goal = ((0,26),(10,26))
goal_helper = ((0,25.5),(10,25.5))
board = build_path([(14,0),(29,4),(31,8),(31,39),(28,42),(18,44),(3,41),(0,22),(6,5),(14,0)]) | build_path([(14,9),(25,11),(25,23),(24,27),(24,35),(18,37),(11,35),(9,33),(10,20),(8,14),(14,9)])

evaluation_function = linedistance

seen = Counter()
shortest = ":)"*15

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
				print("Found something:")
				print(history + [car] + [move])
				shortest = history + [car] + [move]
		else:
			turn(move,history + [car])
	return shortest

print("Car:",car)
print("Goal:",goal)
print("Board:",board)
turn(car,[])