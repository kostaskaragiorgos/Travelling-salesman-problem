"""
Nearest Neighbor
"""
import numpy as np 
import pandas as pd 
from fileparser import fileparser

def findmin(table,node):
    return int (table[node].min() ),  int(table[node].idxmin())


def visitcheck(totalscore,table,number,visited_nodes,current_node,pos_of_min,minofthetable):
    if (str(pos_of_min) in visited_nodes) == False:
        current_node = number[(pos_of_min)]
        visited_nodes.append(current_node)
        totalscore += minofthetable
        return table , totalscore ,current_node , visited_nodes, pos_of_min,minofthetable
    else:
        table =  table.replace(minofthetable,np.nan)
        minofthetable, pos_of_min = findmin(table,current_node)
        return table , totalscore ,current_node , visited_nodes , pos_of_min,minofthetable


def nearserN(table,number):
    totalscore = 0
    current_node = starting_node = number[0] 
    table = table.replace(0,np.nan)
    visited_nodes = []
    visited_nodes.append(starting_node)
    minofthetable, pos_of_min = findmin(table,starting_node)
    while len(visited_nodes) < len(number)+1 :
        if len(visited_nodes) != len(number):
            minofthetable, pos_of_min = findmin(table,current_node)
            table , totalscore , current_node , visited_nodes,pos_of_min,minofthetable =  visitcheck(totalscore,table,number,visited_nodes,current_node,pos_of_min,minofthetable) 
        else:
            table = np.array(table)
            totalscore += table[int(starting_node),int(current_node)]
            visited_nodes.append(starting_node)
    return visited_nodes , totalscore
        
"""
table , number = fileparser("symmetric10nodesexample.txt")
visited_nodes, totalscore = nearserN(table,number)
print("Route:",visited_nodes)
print("Total_score:",totalscore)
"""