"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """

        self.vertices[vertex_id] = set()  #create a set that will hold the edges

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # if the first and second vertices are present
        if v1 in self.vertices and v2 in self.vertices:
            #then add the next node following the previous vertex
            self.vertices[v1].add(v2)
        else:
            raise IndexError("nonexistent vertex")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """

        return self.vertices[vertex_id]
        

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        #create an empty queue
        q = Queue()

        visited = set()     #create empty set to keep track of the already visited vertices

        #initialize, enqueue the starting node
        q.enqueue(starting_vertex)
        #while the queue s not empty
        while q.size() > 0:
            #dequeue the first item
            v = q.dequeue()
            #if it's not been visited
            if v not in visited:
                #mark as visitied(i.e. add to the visited set)
                visited.add(v)
                print(f"Visited {v}")
                #add all neighbors to the queue
                for next_vert in self.get_neighbors(v):
                    q.enqueue(next_vert)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        #implement using a stack

        #make an empty stack
        s = Stack()

        #create empty set to keep track of visited
        visited = set()

        #push to starting vertex
        s.push(starting_vertex)

        #while stack is not empty

        while s.size() > 0:
            #pop off the first item/item that's at the very top. the current_vertex that's visited
            current_vertex = s.pop()

            #if not been visited
            if current_vertex not in visited:
                #mark as visited (add to the visited set)
                visited.add(current_vertex)
                print(f"dft visited {current_vertex}")

                # for each neighboring vertex, add all neighbors into the stack
                for neighbor in self.get_neighbors(current_vertex):
                    #push method created from Stack in util.py file
                        #append method actually used
                    s.push(neighbor)
        


    def dft_recursive(self, starting_vertex, visited = set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        #create a set to keep track of visited nodes
        # visited = set()

        if starting_vertex not in visited:



    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        #implement using a stack

        # Create an empty stack
        s = Stack()

         # and enqueue A PATH TO the starting vertex ID
        # Create a Set to store visited vertices
        visited = set()
        # While the queue is not empty...
        q.enqueue(starting_vertex)
            # Dequeue the first PATH
            # Grab the last vertex from the PATH
            # If that vertex has not been visited...
                # CHECK IF IT'S THE TARGET
                  # IF SO, RETURN PATH
                # Mark it as visited...
                # Then add A PATH TO its neighbors to the back of the queue
                  # COPY THE PATH
                  # APPEND THE NEIGHBOR TO THE BACK


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
