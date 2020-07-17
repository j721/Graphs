from room import Room
from player import Player
from world import World

import random
from ast import literal_eval


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



# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']

#UPER

#To solve this path, you'll want to construct your own traversal graph. 
# You start in room 0, which contains exits ['n', 's', 'w', 'e']. 
#  
# need to create own traversal path- set of directions for player to raver
            # start by initializing empty traversal path
# create a visited set/dictionary to keep track of the visited rooms
            #initialize empty visited set() or {}   
# 
# 
# 
# You know you are done when you have exactly 500 entries (0-499) in your graph  
#and no '?' in the adjacency dictionaries. To do this, 
# you will need to write a traversal algorithm 
# that logs the path into traversal_path as it walks.
# (i.e) meaning seaparate paths/lists needs to made to keep track of the changes
# 
# think of using either bfs (queue)

#  or dfs(stack)
# Start by writing an algorithm that picks a random unexplored direction 
# from the player's current room, travels and logs that direction, then loops. 
# This should cause your player to walk a depth-first traversal. 
# When you reach a dead-end (i.e. a room with no unexplored paths),
#  walk back to the nearest room that does contain an unexplored path.
# 

#initialize to empty lists and dictionary
# traversal_path = [] 
# path = []
# visited = {}
# #create directions
# directions = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}

# #initialize player in current room 
# visited[player.current_room.id] = player.current_room.get_exits()   #get_exits method allows player to change direction (possible exits) from room.py file  

# #keep visiting until all of the rooms have been visited ending at the very last one
# while len(visited) < len(room_graph) -1:   

#     #if the new current room, player is in has not been marked as visited yet
#     if player.current_room.id not in visited:
#         #mark as visited
#         visited[player.current_room.id] = player.current_room.get_exits()
#         #after the path has now been explored
#         #shuffle possible new rooms player can enter into
#         random.shuffle(visited[player.current_room.id])
#         #grab the last direction player is able to move, the dead end
#         last_direction = path[-1]
#         #remove that last direction to be able to repeat the traversal
#         visited[player.current_room.id].remove(last_direction)

#     #if there are no rooms left to explore
#     while len(visited[player.current_room.id]) < 1:
#         #remove the last item from the stack 
#         last_direction = path.pop()
#         #add that direction into our traversal path
#         traversal_path.append(last_direction)
#         #have player player walk backwards of the last direction added to the stack
#         #go in reverse direction to find other unexplored rooms
#         player.travel(last_direction)

#     #having player move

#     #remove the first room/path from the visited 
#     move_direction = visited[player.current_room.id].pop(0)
#     #add that direction again into the traversal path
#     traversal_path.append(move_direction)
#     #add that direction into our original path 
#     path.append(directions[move_direction])
#     #have the player travel with that direction
#     player.travel(move_direction)

#2nd method

#initialize traversal path
traversal_path =[]
#have path be set to empty stack
path = Stack()
#have path start at zeroth index
path.push(0)
#create empty visited set 
visited =set()

#visited rooms less than total number of rooms in the graph (from world.py file)
#keep going until we reach all of the rooms

# while len(visited) < len(room_graph)-1:
while len(visited) < len(room_graph):

    #explored path
    explored_path = Stack() #similar to copy_path create an empty stack to hold our new path of directions
    #grab last item from the stack
    curr = path.stack[-1]
    #mark it as visited
    visited.add(curr)

    #have new moves start at the second direction added, (i.e  index one) 
    new_moves = room_graph[curr][1]

    #for each move, and new_room encountered in new_moves/directions
    for move, next_room in new_moves.items(): #items method to return tuple key-value pair for directions. i.e. (n:s, e:w)
        #if new room has not been explored yet
        if next_room not in visited:
            #add that into our explored path
            explored_path.push(next_room)
    #if explored path is not empty meaning there are unexplored paths being added
    if explored_path.size() > 0:
        #grab the first room from the explored path Stack
        room = explored_path.stack[0]
        #add that room into our original path
        path.push(room)
    #else if there are no unexplored paths available and the visited/explored path is empty
    else:
        # grabbing the second to last room that was from our path
        #can't grab -1, then that would be the end and we would have to update the new dead end in our graph
        room = path.stack[-2]
        #remove it from our path
        #  to be able to reverse backwards to a room that has unexplored paths available 
        path.pop()

    #another condition for each move, new room encountered from our future directions  
    for move, next_room in new_moves.items():
        #if new room is our target room
        if next_room ==  room:
            #then add that into our traversal path
            traversal_path.append(move)





# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
