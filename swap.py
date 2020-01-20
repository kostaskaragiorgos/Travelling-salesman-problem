# swap 
from random import randint
from nearestneighbor import *
import numpy as np

#table , number = fileparser("symmetric10nodesexample.txt")
#table = np.array(table)

def swapPositions(list, pos1, pos2): 
      
    list[pos1], list[pos2] = list[pos2], list[pos1] 
    return list


def swap(visited_nodes,totalscore, tries):
    stop_counter = 0
    current_route = visited_nodes
    current_score = totalscore
    while stop_counter < tries:
        newroute = swapPositions(current_route,randint(1,len(number)-1),randint(1,len(number)-1))
        new_score = 0
        i = 0
        while ( i < len(newroute)-1):
            new_score += table[int(newroute[i]),int(newroute[i+1])]
            i += 1
        if new_score < current_score:
            current_score = new_score
            current_route = newroute 
        else:
            stop_counter += 1
    return current_route , current_score



#current_route , current_score = swap(visited_nodes,totalscore,10000) 
#print("after the usage of swap the best route is :" +str(current_route)+ "with score :"+str(current_score))