from random import randint
import numpy as np

def swapPositions(list, pos1, pos2): 
      
    list[pos1], list[pos2] = list[pos2], list[pos1] 
    return list



    

def swap(visited_nodes,totalscore, tries,table,number):
    stop_counter = 0
    current_route = visited_nodes
    current_score = totalscore
    table = np.array(table)
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

