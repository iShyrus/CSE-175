#
# ucost.py
#
# This file provides a function implementing uniform cost search for a
# route finding problem. Various search utilities from "route.py" are
# used in this function, including the classes RouteProblem, Node, and
# Frontier.
#
# YOUR COMMENTS INCLUDING CITATIONS
#
# YOUR NAME - THE DATE
#

from route import Node
from route import Frontier

def uniform_cost_search(problem, repeat_check=False):
    """Perform uniform cost search to solve the given route finding
    problem, returning a solution node in the search tree, corresponding
    to the goal location, if a solution is found. Only perform repeated
    state checking if the provided boolean argument is true."""

    #gets start and end locations
    start = problem.start
    goal = problem.goal

    # Start and end node
    node = Node(start)
    goal = Node(goal)



    #'g' for ucost search in frontier
    frontier = Frontier(root_node=node, sort_by='g')
    reached = Frontier(root_node=node, sort_by='g')

    # return node if = goal
    if (node == goal):
        return node

    if(repeat_check == False):#if repeat check is false
        while (frontier.is_empty() == False): #while frontier isn't empty
            node = frontier.pop()# pops leaf node
            if (node == goal): #if node is at goal return
                return node
            children = node.expand(problem)#expands child nodes
            for x in children: #goes through children and adds to frontier
                frontier.add(x)

    if (repeat_check == True):  # if repeat check is true
        while (frontier.is_empty() == False):#while frontier isn't empty
            node = frontier.pop() #pops node leaf
            if (node == goal): #if node is goal, return
                return node

            children = node.expand(problem) #expands child node
            for x in children: #goes through children
                if (reached.contains(x) == True): #if reached contains child node
                    if (frontier.contains(x) == True and frontier.__getitem__(x) > x.value()):
                        frontier.__delitem__(x) #removes matching node
                        frontier.add(x) # adds child to frontier
                else:
                        reached.add(x) #adds child to reached and frontier
                        frontier.add(x)


    return None