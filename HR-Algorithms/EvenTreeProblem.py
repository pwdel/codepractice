# https://www.hackerrank.com/challenges/even-tree/problem
#!/bin/python3

# interesting side node - LaTeX based tree generator - https://lautgesetz.com/latreex/

# hint - Tree in graph theory. https://en.wikipedia.org/wiki/Tree_(graph_theory)
# hint - a node is a node, while an edge is the connector between two nodes.
# hint - the root of a tree is always 1

# objective - we are trying to, "snip" the edges so all trees contain an even number of nodes

# how can we tell the number of nodes from an entire graph ...?

# t_to = [1, 1, 3, 2, 1, 2, 6, 8, 8]
# t_from = [2, 3, 4, 5, 6, 7, 8, 9, 10]

import math
import os
import random
import re
import sys

# Complete the evenForest function below.
def evenForest(t_nodes, t_edges, t_from, t_to):
    # the first line of input contains two integers:
    # t_nodes, t_edges - the number of nodes and edges
    # print(t_nodes)
    # print(t_edges)
    # print(t_fron)
    # print(t_to)

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
