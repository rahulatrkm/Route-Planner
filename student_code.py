global intersection_dict, roads_list
def shortest_path(M,start,goal):
    global intersection_dict, roads_list
    print("shortest path called")
    #print(start, goal)
    intersection_dict = M.intersections
    roads_list = M.roads
    current = start
    path = []
    frontiers = {}
    # dictionary for O(1) look up
    explored = {}
    while current != goal:
        # updating frontiers
        for pos_road in road_list[current]:
            # check if explored
            temp = explored.get(pos_road, 0)
            if not temp:
                # dict with g & h value
                frontiers{pos_road} = [(abs(intersection_dict[pos_road][0] - intersection_dict[current][0]) + abs(intersection_dict[pos_road][1] - intersection_dict[current][1])), (abs(intersection_dict[pos_road][0] - intersection_dict[goal][0]) + abs(intersection_dict[pos_road][1] - intersection_dict[goal][1]))]
        
        min_f = float('inf')
        min_f_idx = 0
        for curr_front in frontiers:
            if sum(frontiers[curr_front]) < min_f:
                min_f_idx = curr_front
    return

def calc_min(current, frontiers):
    global intersection_dict, roads_list
    min_f = 0
    g = []
    h = []
    for 