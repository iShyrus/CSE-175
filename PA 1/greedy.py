#
# greedy.py
#
# This file provides a function implementing greedy best-first search for
# a route finding problem. Various search utilities from "route.py" are
# used in this function, including the classes RouteProblem, Node, and
# Frontier. Also, this function uses heuristic function objects defined
# in the "heuristic.py" file.
#
# YOUR COMMENTS INCLUDING CITATIONS
#
# YOUR NAME - THE DATE
#


from route import Node
from route import Frontier


def greedy_search(problem, h, repeat_check=False):
    """Perform greedy best-first search to solve the given route finding
    problem, returning a solution node in the search tree, corresponding
    to the goal location, if a solution is found. Only perform repeated
    state checking if the provided boolean argument is true."""



    #gets start and end locations
    start = problem.start
    goal = problem.goal

    #Start and and end node
    node = Node(start)
    goal = Node(goal)

    #'h' for greedy search in frontier
    frontier = Frontier(node, 'h')
    reached = Frontier(node, 'h')


    #return node if = goal
    if (node == goal):
        return node

    # h = Greedy Search
    frontier = Frontier(root_node=node, sort_by='h')
    reached = Frontier(root_node=node, sort_by='h')



    #while frontier isn't empty
    while (frontier.is_empty() == False):
        node = frontier.pop() #pops leaf
        if (node == goal): #if node is at goal return
            return node
        children = node.expand(problem, h) #expands child nodes

        #goes through all children
        for n in children:

            #Checks for repeat check
            if(repeat_check ==False):
                frontier.add(n) #add child to frontier
            else:
                if (reached.contains(n) == False):
                    reached.add(n) #add child to frontier and reached
                    frontier.add(n)

    return None