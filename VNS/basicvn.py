

from nearestneighbor import *
from swap import *
from relocate import *
from _2_opt import _2optf,partial_reverse

"""
table , number = fileparser("40node.txt")
nearestnnodes, nearestscore = nearserN(table,number)
print("NearestnRoute:",nearestnnodes)
print("Nearestn_score:",nearestscore)

currentbestscore = nearestscore
currentbestnode = nearestnnodes


lista  = [relocatef(currentbestnode, currentbestscore , 1000,table,number),_2optf(currentbestnode,currentbestscore, 1000,table,number)]
"""
def bvns(currentbestnode,currentbestscore,listofne ,tries):
    f = 0 
    j = 0
    while j < tries:
        for i in range(len(listofne)):
            if f ==1 :    
                new_route , new_score = listofne[0]
            else:
                new_route , new_score = listofne[i]
            if new_score < currentbestscore:
                currentbestnode = new_route
                currentbestscore = new_score
                f = 1
                if f == 1:
                    new_route , new_score = listofne[0]
            else:
                f = 0
                if i ==1:
                    new_route , new_score = listofne[0]                
                else:
                    new_route , new_score = listofne[i+1]
        j +=1
    return  new_route,new_score
"""
new_route , new_score  = bvns(currentbestnode,currentbestscore,lista,1000)
print(new_route,new_score)
"""