from geometry import build_path

car = (4,25,0,-1)
goal = ((0,26),(10,26))
goal_helper = ((0,25.5),(10,25.5))
board = build_path([(14,0),(29,4),(31,8),(31,39),(28,42),(18,44),(3,41),(0,22),(6,5),(14,0)]) | build_path([(14,9),(25,11),(25,23),(24,27),(24,35),(18,37),(11,35),(9,33),(10,20),(8,14),(14,9)])