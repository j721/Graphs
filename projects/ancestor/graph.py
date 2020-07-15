"""
Simple graph implementation
"""


class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set() #create a set that will hold the edges

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
        # create empty queue
        q = Queue()
        #  #initialize, enqueue the starting node
        q.enqueue(starting_vertex)

        #create empty set to keep track of the already visited vertices
        visited = set()

        # while queue not empty
        while q.size() > 0:
            # dequeue first item
            current_node = q.dequeue()

            # if it's not been visited
            if current_node not in visited:
                print(current_node)
                # mark as visited
                visited.add(current_node)
                # get neighbors
                neighbors = self.get_neighbors(current_node)
                # for each of the neighbors
                # add all neighbors to the queue
                for neighbor in neighbors:
                    # add to the queue
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        #make an empty stack
        s = Stack()
       
        #push to starting vertex
        s.push(starting_vertex)

       #create empty set to keep track of visited
        visited = set()

        # while our stack is not empty
        while s.size() > 0:
             #pop off the first item/item that's at the very top. the current_vertex that's visited
            current_vertex = s.pop()

           #if not been visited
            if current_vertex not in visited:
                print(current_vertex)
                # mark as visited
                visited.add(current_vertex)
                # get its neighbors
                neighbors = self.get_neighbors(current_vertex)
                # for each neighboring vertex, add all neighbors into the stack
                for neighbor in neighbors:
                    # add to our stack
                    #push method created from Stack in util.py file
                        #append method actually used
                    s.push(neighbor)
       
    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        # #if not in visited  
        if starting_vertex not in visited:
            # mark as visited
            visited.add(starting_vertex)
            # #print out visited vertices
            print(starting_vertex)

            #for each neighbor in vertices 
            for neighbor in self.vertices[starting_vertex]:
                #call function recursively.
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
       # Create an empty queue
        q = Queue()

        # enqueue A PATH TO the starting vertex 
        q.enqueue([starting_vertex])

        visited = set()  # create a Set to store visited vertices
        
        
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first PATH
            path = q.dequeue()
            # Grab the last vertex from the PATH
            last_vertex = path[-1]
            # If that vertex has not been visited...
            if last_vertex not in visited:
                # CHECK IF IT'S THE TARGET 
                if last_vertex == destination_vertex:
                  # IF SO, RETURN PATH
                    return path
                #mark as visited and add to visited set
                visited.add(last_vertex)


                # Then add A PATH TO its neighbors to the back of the queue
                for neighbor in self.vertices[last_vertex]:
                  # COPY THE PATH
                  copied_path = path.copy()
                  # APPEND THE NEIGHBOR TO THE BACK
                  copied_path.append(neighbor)
                  #enqueue to the new path
                  q.enqueue(copied_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # implement empty stack
        s = Stack()
        # push a path to the starting vertex
        s.push([starting_vertex])
        # create a set to keep track of all visited nodes
        visited = set()

        # while stack is not empty
        while s.size() > 0:
            # pop the first path
            path = s.pop()
            # get the last vertex from the path
            node = path[-1]

            # if the node hasn't been visited
            if node not in visited:
                # is it our target?
                if node == destination_vertex:
                    # if yes, return path
                    return path
                
                # mark the node as visited
                visited.add(node)

                # add a path to its neighbors
                for neighbor in self.vertices[node]:
                    # copy the path
                    new_path = path.copy()
                    # append the neighbor
                    new_path.append(neighbor)
                    s.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=set(), path=[]):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        This should be done using recursion.
        """
       #add starting vertex into visited set
        visited.add(starting_vertex)
        #add path for starting vertex
        path = path + [starting_vertex]
        #if vertex is our target
        if starting_vertex == destination_vertex:
            #return the path
            return path
        # for each of the vertex's neighbor
        for neighbor in self.get_neighbors(starting_vertex):
            #if node has not been visited:
            #recursion and look for a new path to search
            if neighbor not in visited:
                new_path = self.dfs_recursive(neighbor, destination_vertex, visited, path)
                # if new_path is not None return it
                if new_path is not None:
                    return new_path

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
    # print(graph.vertices)

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