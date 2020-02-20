"""
File Parser for tsp problems
"""
import numpy as np
import pandas as pd
def fileparser(filename):
    """
    inputs: filename --> the .txt file of the tsp problem
    return : the table and columns 
    """
    file = np.loadtxt(filename)
    df = pd.DataFrame(file)
    node_no = len(df)
    c = [str(n) for n in range(node_no)]
    df = pd.DataFrame(file, columns=c)
    return df, c


#table , number = fileparser("symmetric10nodesexample.txt")
#print(table,number)
