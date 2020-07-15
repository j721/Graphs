
"""

Suppose we have some input data describing a graph of relationships between parents and children over multiple generations.
 The data is formatted as a list of (parent, child) pairs, 
 where each individual is assigned a unique integer identifier.

Write a function that, given the dataset and the ID of an individual in the dataset, 
returns their earliest known ancestor – the one at the farthest distance from the input individual.

If there is more than one ancestor tied for "earliest", return the one with the lowest numeric ID. 
If the input individual has no parents, the function should return -1.


Clarifications:

The input will not be empty.
There are no cycles in the input.
There are no "repeated" ancestors – if two individuals are connected, it is by exactly one path.
IDs will always be positive integers.
A parent may have any number of children.


"""


def earliest_ancestor(ancestors, starting_node):
    # set default target node to None
    target_node = None
    #for every node in the ancestors graph
    for node in ancestors:
        # found node as a child in a node pair
        if starting_node is node[1]:
            target_node = node
            break
    #if target_node that we are looking at has no parents then return -1
    if target_node is None:
        return -1

    #create empty set to keep track of visited
    visited = set()
    #create empty stack
    stack = []
    #initialize stack with a pair
    stack.insert(0, target_node)

    #if stack is not empty
    while len(stack) > 0:
        #pop off the first item from the stack 
        node = stack.pop(0)
        # check if node is parent to starting node
        parent = node[0]
        #node has not been visited, then mark as visited
        if node not in visited:
            visited.add(node)
            # find a parent pointing to the already visited node
            for ancestor in ancestors:
                # a parent node pointing to another parent
                if ancestor[1] is parent:
                    # add ancestor to stack
                    stack.append(ancestor)
                    break
    return parent


