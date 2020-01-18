from random import randint
from nearsetneighbor import *
import numpy as np

def relocate(array ,pos_to_move , pos_where_to_be):
    to_move = array.index(array[pos_to_move])
    array.insert(pos_where_to_be,array.pop(to_move))
    return array



#table , number = fileparser("symmetric10nodesexample.txt")
#visited_nodes, totalscore = nearserN(table,number)


def relocatef(visitednode,totalscore,tries,table,number):
    stop_counter = 0
    current_route = visitednode
    current_score = totalscore
    table = np.array(table)
    while stop_counter < tries:
        newroute =  relocate(current_route,randint(1,len(number)-1),randint(1,len(number)-1))
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

#current_route , current_score  =relocatef(visited_nodes , totalscore , 1000,table,number)
#print(current_route,current_score)
    