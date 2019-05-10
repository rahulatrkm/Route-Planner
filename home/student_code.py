global intersection_dict, roads_list
def shortest_path(M,start,goal):
    global intersection_dict, roads_list
    print("shortest path called")
    #print(start, goal)
    intersection_dict = M.intersections
    roads_list = M.roads
    current = start
    path = []
    frontiers = [start]
    explored = []
    while current != goal:
    return

def calc_min(current, frontiers):
    global intersection_dict, roads_list