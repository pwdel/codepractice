# https://www.hackerrank.com/challenges/even-tree/problem

# interesting side node - LaTeX based tree generator - https://lautgesetz.com/latreex/

# hint - Tree in graph theory. https://en.wikipedia.org/wiki/Tree_(graph_theory)
# hint - a node is a node, while an edge is the connector between two nodes.
# hint - the root of a tree is always 1

# objective - we are trying to, "snip" the edges so all trees contain an even number of nodes

# t_to = [1, 1, 3, 2, 1, 2, 6, 8, 8]
# t_from = [2, 3, 4, 5, 6, 7, 8, 9, 10]

# hint - range has the ability to put a step size, including a negative step size.
# range(start, stop, step)

# hint, "in", in python checks if a value is within a list.
# fruits = ["apple", "banana", "cherry"]
# if "banana" in fruits:
#  print("yes")

# How this works:
# First, we find all leaf nodes. All nodes are assigned by default a weight of zero.
# Note that the leafs can be found lower down the lists, as the lists make assignment sequentially
# so, iterate backwards to start off.
# We use a dictionary to assign weights, so just put no entry. - weight={}
# Find the leaf nodes by 1) Assign a value of, 1 to the dictionary key for each node, starting with t_from.
# then with t_to, which is the connecting node for each value we're going through at, "i"
# also assign 1 if just starting out in the, "weight" list (by assigning the t_to its child's value).
# however, for every t_to thereafter, as i continues, add an additional 1.
# logically, leafs will have a value of 1, parents will have a value above 1.
# note, since nodes are being assigned their child's value, any children which have a higher than 1 value
# will retain information about how much is below them, that value is being, "passed up" the tree branch.
# note that parents will also get a +1 in addition to the nodes below them, to count itself.

# then, you will have a table of weights showing how many are below each node on the tree.
# any node with an even value has an even number of nodes (including itself)


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the evenForest function below.
def evenForest(t_nodes, t_edges, t_from, t_to):
    weight={}
    print('weight starts out as: ',weight,'which is type',type(weight))
    print('stepping through from t_edges-1 down through 0 by -1 increments')
    for i in range(t_edges-1,-1,-1):
        print('----------')
        print('now evaluating i=',i)
        print('***checking the t_from...')
        if t_from[i] in weight:
            print('found that value: ',t_from[i],'is in weight, as: ',weight)
            weight[t_from[i]]+=1
        else:
            weight[t_from[i]]=1
            print('if t_from[i]: ',t_from[i],'is not in weight, currently : ',weight)
            print('...then set the weight value @ [t_from[i]] : ',[t_from[i]],'to',1)
        print('***checking the t_to...')
        if t_to[i] in weight:
            print('found that value: ',t_to[i],'is in weight, as: ',weight)
            weight[t_to[i]]+=weight[t_from[i]]
        else:
            print('if t_to[i]: ',t_to[i],'is not in weight, currently : ',weight)
            print('...then set the weight value @ [t_to[i]] : ',[t_to[i]],'to the weight value at t_from[i], which is: ',weight[t_from[i]])
            weight[t_to[i]]=weight[t_from[i]]

    print('weight is...',weight)
    print('result...')

    evenlist=[]
    for key in weight:
        print('going through keys in weight, now at: ',key)
        if weight[key]%2==0:
            print('found weight[key]%2==0, which means even weight above: ',key)
            evenlist.append(1)

    print('now our list of even cut points is:',evenlist)
    print('length of length of cut points: ',len(evenlist),'which is our answer.')

    return(len(evenlist))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t_nodes, t_edges = map(int, input().rstrip().split())

    t_from = [0] * t_edges
    t_to = [0] * t_edges

    for i in range(t_edges):
        t_from[i], t_to[i] = map(int, input().rstrip().split())

    res = evenForest(t_nodes, t_edges, t_from, t_to)

    fptr.write(str(res) + '\n')

    fptr.close()
