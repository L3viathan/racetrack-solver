def line_intersection(l1,l2):
	'''returns True iff l1 crosses l2'''
	return ((ccw(l1[0],l1[1],l2[0])*ccw(l1[0],l1[1],l2[1]))<=0) and ((ccw(l2[0],l2[1],l1[0])*ccw(l2[0],l2[1],l1[1]))<=0)

def ccw(p0,p1,p2):
 dx1 = p1[0]-p0[0]
 dy1 = p1[1]-p0[1]
 dx2 = p2[0]-p0[0]
 dy2 = p2[1]-p0[1]
 if dx1*dy2 > dy1*dx2: return 1
 if dx1*dy2 < dy1*dx2: return -1;
 if dx1*dy2 == dy1*dx2:
   if (dx1*dx2<0) or (dy1*dy2<0): return -1
   if (dx1*dx1+dy1*dy1) >= (dx2*dx2+dy2*dy2): return 0
 return 1
 
def build_path(listofpoints):
    return set(zip(listofpoints[:-1],listofpoints[1:]))

def distance(pos1,pos2):
    return abs(pos1[0]-pos2[0]) + abs(pos1[1]-pos2[1])

def linedistance(pos1,line):
    pos2 = middle_point(line)
    return abs(pos1[0]-pos2[0]) + abs(pos1[1]-pos2[1])

def middle_point(line):
    return ((line[0][0]+line[1][0])/2,(line[0][1]+line[1][1])/2)