import route
import main
from route import Node
from route import Frontier


def BFS(problem, repeat_check=False):
    """Perform breadth-first search to solve the given route finding
    problem, returning a solution node in the search tree, corresponding
    to the goal location, if a solution is found. Only perform repeated
    state checking if the provided boolean argument is true."""

    # test_______________________________
    # print(node)
    # print(problem)
    # print(node.expand(problem))
    # childs = node.expand(problem)
    # print(childs)
    # print(childs[1])
    # print(childs[1].expand(problem))
    #
    # for x in childs:
    #     print(x)

    # print(frontier)
    # test_______________________________

    #Gets start and goal and puts in node class
    node = Node(problem.start)
    goal = Node(problem.goal)


    if(node == goal):
        return node

    #Creating frontier/reached, True because of bfs
    frontier = Frontier(node, queue=True)
    reached = Frontier(node, queue=True)



    while(frontier.is_empty() != True):     #while frontier is not empty
        node = frontier.pop() #removes leaf
        if(node == goal):   #checks if goal met
            return node
        childs = node.expand(problem) #children of current node

        for child in childs:    #repeats through child, checks if repeat check is true/false, adds to frontier/reached
            if(repeat_check == True):
                if(reached.contains(child) == False):
                    reached.add(child)
                    frontier.add(child)
            elif(repeat_check == False):
                frontier.add(child)

    return None
