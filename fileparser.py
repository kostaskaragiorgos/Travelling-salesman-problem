import numpy as np 
import pandas as pd 
import random as rd
 

def fileparser(filename):
    """
    inputs: filename --> the .txt file of the tsp problem
    return : the table and columns 
    """
    file = np.loadtxt(filename)
    df = pd.DataFrame(file)
    node_no = len(df)
    c = [str(n) for n in range(node_no)]
    df = pd.DataFrame(file, columns  = c)
    return df , c


table , number = fileparser("5nodetsp.txt")
print(table,number)

print(table.iloc[0])
totalscore = 0

starting_node = number[0] 
table = table.replace(0,np.nan)
minvof0 = table[starting_node].min()
minpos0 = table[starting_node].idxmin()
print(minvof0)
print(minpos0)
visited_nodes = []
visited_nodes.append(starting_node)
print(visited_nodes)
if (str(minpos0) in visited_nodes) == False:
    print("yes you can visit")
    current_node = number[(minpos0)]
    visited_nodes.append(current_node)
    totalscore += minvof0
else:
    print("no")
    
print(current_node)
print(visited_nodes)

minvof4 = table[current_node].min()
minpos4 = table[current_node].idxmin()
print(minvof4)
print(minpos4)

if (str(minpos4) in visited_nodes) == False:
    print("yes you can visit")
    current_node = number[(minpos4)]
    visited_nodes.append(current_node)
    totalscore += minvof4
else:
    print("no")
    table = table.replace(minvof4,np.nan)
    
minvof4 = table[current_node].min()
minpos4 = table[current_node].idxmin()
print(minvof4)
print(minpos4)

if (str(minpos4) in visited_nodes) == False:
    print("yes you can visit")
    current_node = number[(minpos4)]
    visited_nodes.append(current_node)
    totalscore += minvof4
else:
    print("no")
    table = table.replace(minvof4,np.nan)
    
    
print(current_node)
print(visited_nodes)

minvof1 = table[current_node].min()
minpos1 = table[current_node].idxmin()
print(minvof1)
print(minpos1)
    
if (str(minpos1) in visited_nodes) == False:
    print("yes you can visit")
    current_node = number[(minpos1)]
    visited_nodes.append(current_node)
    totalscore += minvof1
else:
    print("no")
    table = table.replace(minvof1,np.nan)

print(current_node)
print(visited_nodes)

minvof2 = table[current_node].min()
minpos2 = table[current_node].idxmin()
print(minvof2)
print(minpos2)

if (str(minpos2) in visited_nodes) == False:
    print("yes you can visit")
    current_node = number[(minpos2)]
    visited_nodes.append(current_node)
    totalscore += minvof2
else:
    print("no")
    table = table.replace(minvof1,np.nan)

print(current_node)
print(visited_nodes)

table = np.array(table)
totalscore += table[int(starting_node),int(current_node)]
visited_nodes.append(starting_node)
print("Route:",visited_nodes)
print("Total_score:",totalscore)
print(table)