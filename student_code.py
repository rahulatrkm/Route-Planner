import math

global intersection_dict, roads_list, pos_path, heuristic_values
heuristic_values = {}
intersection_dict = {}
roads_list = []
pos_path = []

class  Priority_queue(object):
    """docstring for  Priority_queue."""
    def __init__(self):
        self.queue = []
    def __str__(self):
        return ' '.join([str(i) for i in self.queue])
    def isEmpty(self):
        return not self.queue
    def insert(self, data):
        self.queue.append(data)
    def delete(self):
        try:
            mini = 0
            for i in range(len(self.queue)):
                if (self.queue[i][-1]+self.queue[i][-2]) < (self.queue[mini][-1] + self.queue[mini][-2]):
                    mini = i
            item = self.queue[mini]
            del self.queue[mini]
            return item
        except IndexError:
            print()

def shortest_path(M, start, goal):
    if start == goal:
        return [start]
    
    #print(M, start,goal)
    global intersection_dict, roads_list, pos_path, heuristic_values
    heuristic_values = {}
    for node in intersection_dict:
        #print(node)
        heuristic_values[node] = math.sqrt((intersection_dict[node][0] - intersection_dict[goal][0])**2 + abs(intersection_dict[node][1] - intersection_dict[goal][1])**2)
        
    #print(heuristic_values)
    print("shortest path called")
    intersection_dict = M.intersections
    roads_list = M.roads
    pos_path = Priority_queue()
    pos_path.insert([[start],0,heuristic_values[start]])
    return helper_path(start, goal)

def helper_path(current, goal):
    global intersection_dict, roads_list, pos_path, heuristic_values
    #print(pos_path)
    #print()
    # handling if there is no any path
    item = 0
    if pos_path.isEmpty():
        return "No possible path"
    else:
        item = pos_path.delete()
    #print(item, "item")
    current = item[0][-1]
    if current == goal:
        return item[0]

    #print(roads_list[current], 'road')
    for front in roads_list[current]:
        if front in item[0]:
            continue
        #print(pos_path, "in for", front)
        g = math.sqrt((intersection_dict[front][0] - intersection_dict[current][0])**2 + (intersection_dict[front][1] - intersection_dict[current][1])**2) + item[-2]
        h = heuristic_values[front]
        pos_path.insert([item[0]+[front],g,h])

    return helper_path(current, goal)
