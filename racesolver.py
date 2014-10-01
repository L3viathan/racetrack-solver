import sys

from geometry import line_intersection
from collections import Counter
from time import sleep

# car = (21,2,0,2)
# goal = (5,22)
# board = {((0,0),(23,0)),((23,0),(23,10)),((23,10),(18,17)),((18,17),(5,17)),((5,17),(5,19)),((5,19),(9,24)),((9,24),(0,24)),((0,24),(0,0))}

# car = (17,3,-1,0)
# goal = (2,22)
# board = {((0,0),(18,0)),((18,0),(18,6)),((18,6),(5,6)),((5,6),(5,12)),((5,12),(7,15)),((7,15),(16,15)),((16,15),(16,25)),((16,25),(0,25)),((0,25),(0,0)),((0,19),(5,19))}

car = (2,1,0,1)
goal = ((4,1),(9,1))
board = (((0,0),(9,0)),((9,0),(9,7)),((9,7),(0,7)),((0,7),(0,0)),((4,0),(4,4)))

def moves(car,board):
	'''Returns all possible legal moves for a given car'''
	for x in range(-1,2,1):
		for y in range(-1,2,1):
			new = (car[0] + x + car[2], car[1] + y + car[3], car[2] + x, car[3] + y)
			line = ((car[0],car[1]),(new[0],new[1]))
			#print(line)
			#collision detection
			if any([line_intersection(line,edge) for edge in board]):
				continue
			yield new

def distance(pos1,pos2):
	return abs(pos1[0]-pos2[0]) + abs(pos1[1]-pos2[1])

evaluation_function = distance

seen = Counter()
shortest = [1]*30

def turn(car,history):
	global shortest
	global seen
	if car in seen and seen[car] <= len(history):
		return
	else:
		seen[car] = len(history)
	if len(history)+1 >= len(shortest):
		return
	if (car[0] == goal[0] and car[1] == goal[1]):
		#we found it!
		print("Found solution of length",len(history)+1)
		print(history + [car])
		return history + [car]
		#sys.exit(0)
	current_distance = distance(car,goal)
	possible_moves = [x for x in moves(car,board) if distance(x,goal) < current_distance]
	for move in possible_moves:
	# for move in moves(car,board):
		solution = turn(move,history + [car])
		if solution is not None and (shortest is None or len(solution) < len(shortest)):
			shortest = solution
	return shortest

turn(car,[])
# i = 1
# while True:
#     print("Trying size",i)
#     i += 1
#     shortest = [1]*i
#     seen = Counter()
#     r = turn(car,[])
#     if r != [1]*i:
#         print("Found a solution")
#         break