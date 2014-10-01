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