#
# dfs.py
#
# This file provides a function implementing depth-first search for a
# route-finding problem. Various search utilities from "route.py" are
# used in this function, including the classes RouteProblem, Node, and
# Frontier.
# 
# YOUR COMMENTS INCLUDING CITATIONS
#
# YOUR NAME - THE DATE
# 


from route import Node
from route import Frontier


def DFS(problem, repeat_check=False):
    """Perform depth-first search to solve the given route finding
    problem, returning a solution node in the search tree, corresponding
    to the goal location, if a solution is found. Only perform repeated
    state checking if the provided boolean argument is true."""
    # Gets start and goal and puts in node class

    node = Node(problem.start)
    goal = Node(problem.goal)

    if (node == goal):
        return node

    # Creating frontier/reached, False because of dfs
    frontier = Frontier(node, queue=False)
    reached = Frontier(node, queue=False)

    while (frontier.is_empty() != True):  # while frontier is not empty
        node = frontier.pop()  # removes leaf
        if (node == goal):  # checks if goal met
            return node
        childs = node.expand(problem)  # children of current node

        for child in childs:  # repeats through child, checks if repeat check is true/false, adds to frontier/reached
            if (repeat_check == True):
                if (reached.contains(child) == False):
                    reached.add(child)
                    frontier.add(child)
            elif (repeat_check == False):
                frontier.add(child)

    return None

    return None
