
import math

SCREEN = [["O" for i in range(20)] for x in range(20)] #creates a 10 by 10 grid for the pathfinding to occur on

def heuristic(current_node,target_node):
    dx = abs(target_node[0]-current_node[0])
    dy = abs(target_node[1]-current_node[1])

    diagonal_distance = min(dx,dy)*14
    horizontal_distance = abs(dx-dy)*10

    return diagonal_distance+horizontal_distance #assumes octile 8 way movement

def a_star(start_node,target_node,screen_size_x,screen_size_y): #conditions - target node and start node must be within the dimensions of screen_size_x*screen_size_y
    adjacent_nodes = [(0,-1),(0,1),(1,1),(1,0),(-1,-1),(1,-1),(-1,1),(-1,0)]
    OPEN_SET = [] #OPEN_SET and CLOSED_SET elements will have the form (node,g cost,h cost,f cost,parent node)
    CLOSED_SET = []

    OPEN_SET.append((start_node,0,heuristic(start_node,target_node),heuristic(start_node,target_node),None)) #add the start node to the open set
    while OPEN_SET != []:
        current_node = min(OPEN_SET,key=lambda x:x[3])
        OPEN_SET.remove(current_node)
        CLOSED_SET.append(current_node)

        if current_node[0] == target_node:
            path = [target_node]          #this means you are at the end of the path now
            while current_node[0] != start_node:
                current_node = current_node[4]
                current_node = list(filter(lambda x: x[0] == current_node,CLOSED_SET))[0]
                path.append(current_node[0])
            return path
        
        else:
            for node in adjacent_nodes:
                child_node = (current_node[0][0] + node[0],current_node[0][1] + node[1])
                if 0 <= child_node[0] < screen_size_x and 0 <= child_node[1] < screen_size_y and child_node not in list(map(lambda x: x[0],CLOSED_SET)) : #bounds checking to make sure that an adjacent node exists within the board
                    #calculating the g value
                    if node[0] == 0 or node[1] == 0:
                        g_cost = 10
                    else:
                        g_cost = 14 # g_costs are rounded to 10 and 14 but the real values are 1 and root(2) ~ 1.4
                    g_cost += current_node[1]
                    h_cost = heuristic(child_node,target_node)

                    if child_node in list(map(lambda x: x[0],OPEN_SET)):
                       if list(filter(lambda x: x[0] == child_node,OPEN_SET))[0][1] <= g_cost:
                          continue
                       else:
                           old_node = filter(lambda x: x[0] == child_node,OPEN_SET)
                           old_node = list(old_node)[0]
                           OPEN_SET.remove(old_node)
                    OPEN_SET.append((child_node,g_cost,h_cost,g_cost+h_cost,current_node[0]))

    return -1



path = (a_star((1,1),(5,6),5,6))
if path == -1:
    print("invalid start node or target node")
    exit()
for node in path:
    SCREEN[node[1]][node[0]] = 'X'

for line in SCREEN:
    print(line)






