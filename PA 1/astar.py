#
# astar.py
#
# This file provides a function implementing A* search for a route finding
# problem. Various search utilities from "route.py" are used in this function,
# including the classes RouteProblem, Node, and Frontier. Also, this function
# uses heuristic function objects defined in the "heuristic.py" file.
#
# YOUR COMMENTS INCLUDING CITATIONS
#
# YOUR NAME - THE DATE
#


import route
import main
from route import Node
from route import Frontier
from heuristic import HeuristicFunction
from route import RouteProblem
from route import RoadMap

def a_star_search(problem, h, repeat_check=False):
    """Perform A-Star search to solve the given route finding problem,
    returning a solution node in the search tree, corresponding to the goal
    location, if a solution is found. Only perform repeated state checking if
    the provided boolean argument is true."""

    #gets start and end locations
    start = problem.start
    goal = problem.goal

    #Start and and end node
    node = Node(start)
    goal = Node(goal)


    #'f' for A Star search in frontier
    frontier = Frontier(root_node=node, sort_by='f')
    reached = Frontier(root_node=node, sort_by='f')

    #return node if = goal
    if (node == goal):
        return node


    #while frontier isn't empty
    while (frontier.is_empty() == False):
        node = frontier.pop()#pops leaf
        if (node == goal):#if node is at goal return
            return node

        children = node.expand(problem)#expands child nodes

        #goes through all children
        for n in children:
            if (reached.contains(n) == True): #checks if reached contains child
                if (frontier.contains(n) == True and frontier.__getitem__(n) > n.value()):
                    frontier.__delitem__(n) #remove matching node
                    frontier.add(n) #adds to frontier
            else:

                #Checks for repeat_check
                if (repeat_check == True):
                    reached.add(n)   #adds child to frontier and reached
                    frontier.add(n)
                else:
                    frontier.add(n) #adds to frontier if repeat_check is false

    return None










