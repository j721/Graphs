import random #import random module
import time

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

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.reset()
        print("something completely different")

    def reset(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            return False
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            return False
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

        return True

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    # def populate_graph(self, num_users, avg_friendships):
    #     """
    #     Takes a number of users and an average number of friendships
    #     as arguments

    #     Creates that number of users and a randomly distributed friendships
    #     between those users.

    #     The number of users must be greater than the average number of friendships.
    #     """
    #     # Reset graph
    #     self.reset()
    #     # !!!! IMPLEMENT ME

    #     # Add users
    #     for i in range(num_users):
    #         self.add_user(f"User{i}")

    #     # Create friendships
    #     possible_friendships = [] #create list of possible friends (edges)

    #     for user_id in self.users:
    #         for friend_id in range(user_id + 1, self.last_id +1):#
    #             possible_friendships.append((user_id, friend_id))
        
    #     #shuffle possible friendship
    #     random.shuffle(possible_friendships)

    #     #add friendships
    #     for i in range(num_users * avg_friendships//2):
    #         friendship = possible_friendships[i]
    #         #create a tuple
    #         self.add_friendship(friendship[0], friendship[1])

    #2nd method
    def populate_graph(self, num_users, avg_friendships):

        #reset graph
        self.reset()  

        #add users
        for i in range(num_users):
            self.add_user(f"user {i +1}")
        
        #create friendships
        target_friendships = num_users * avg_friendships
        total_friendships = 0

        while total_friendships < target_friendships:
            user_id = random.randint(1, self.last_id)
            friend_id = random.randint(1, self.last_id)

            if self.add_friendship(user_id, friend_id): #everytime we can add a friendship, we have two friends. One from the user and other new friend user
                total_friendships +=2
            
           


    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """

        #bft

        q = Queue()

        visited = {}

        q.enqueue([user_id])

        while q.size() > 0:
            path = q.dequeue() #grab the last user id

            u = path[-1]

            if u not in visited:
                visited[u] = path

                for neighbor in self.friendships[u]:
                    #need to enqueue the entire path so far, so make a copy of the path
                    path_copy = list(path)
                    path_copy.append(neighbor)
                    q.enqueue(path_copy)

        return visited

            
        # visited = {}  # Note that this is a dictionary, not a set
        # # !!!! IMPLEMENT ME

        # #have user_id be stored in a queue
        # queue = [user_id]
        # #have visited dictionary contain user_id
        # visited[user_id] = [user_id]
        # #if queue is not empty
        # while len(queue) > 0:
        #     #remove the first node from the queue
        #     node = queue.pop()
        #     #grab the friends/edges
        #     friends = self.friendships[node]
        #     #if user in friends list
        #     for user in friends:
        #         if  user not in visited:
        #             #mark as visited and add other visited node(friend)
        #             visited[user] = visited[node] + [user]
        #             #update queue with the user
        #             queue.append(user)
        # return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(f"friendships: {sg.friendships}")
    connections = sg.get_all_social_paths(1)
    print(f"connections: {connections}")
