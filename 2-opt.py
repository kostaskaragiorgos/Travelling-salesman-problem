from random import randint
from nearsetneighbor import *
import numpy as np

def partial_reverse(list_, from_, to):
    if int(from_) < int(to):
        for i in range(0, int((to - from_)/2)):
            (list_[from_+i], list_[to-i]) = (list_[to-i], list_[from_+i])
    else:
        for i in range(0, int((from_ - to)/2)):
            (list_[to+i], list_[from_-i]) = (list_[from_-i], list_[to+i])
    return list_


def _2optf(visitednode,totalscore,tries,table,number):
    stop_counter = 0
    current_route = visitednode
    current_score = totalscore
    table = np.array(table)
    while stop_counter < tries:
        newroute =  partial_reverse(current_route,randint(1,len(number)-1),randint(1,len(number)-1))
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

#current_route , current_score  = _2optf(visited_nodes , totalscore , 10000,table,number)
#print(current_route,current_score)