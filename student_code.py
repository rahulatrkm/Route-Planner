import math

global intersection_dict, roads_list, pos_path
intersection_dict = {}
roads_list = []
pos_path = []
def shortest_path(M, start, goal):
    if start == goal:
        return [start]
    #print(M, start,goal)
    global intersection_dict, roads_list, pos_path
    print("shortest path called")
    intersection_dict = M.intersections
    roads_list = M.roads
    pos_path = [[[],0,math.sqrt((intersection_dict[start][0] - intersection_dict[goal][0])**2 + abs(intersection_dict[start][1] - intersection_dict[goal][1])**2)]]
    helper_path(start, goal)
    if pos_path:
        return pos_path[0][0]
    else:
        return "No possible path"

def helper_path(current, goal):
    global intersection_dict, roads_list, pos_path
    #print(pos_path)
    if not pos_path[0][0]:
        pos_path[0][0].append(current)
    elif pos_path[0][0][-1] == goal:
        return
    
    #print(roads_list[current], 'road')
    for front in roads_list[current]:
        if front in pos_path[0][0]:
            continue
        #print(pos_path, "in for", front)
        g = math.sqrt((intersection_dict[front][0] - intersection_dict[current][0])**2 + (intersection_dict[front][1] - intersection_dict[current][1])**2) + pos_path[0][-2]
        h = math.sqrt((intersection_dict[front][0] - intersection_dict[goal][0])**2 + abs(intersection_dict[front][1] - intersection_dict[goal][1])**2)
        pos_path.append([pos_path[0][0]+[front],g,h])
    
    del pos_path[0]
    # handling if there is no any path
    if not pos_path:
        return
    pos_path = sorted(pos_path, key = lambda x: x[1]+x[2])
    helper_path(pos_path[0][0][-1], goal)
