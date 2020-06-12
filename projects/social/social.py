import random

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
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # Add users
        for i in range(0, num_users):
            self.add_user(f"User {i}")
        # Create Frienships
        # Generate all possible friendship combinations
        possible_friendships = []
        # Avoid duplicates by ensuring the first number is smaller than the second
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))
            # Shuffle the possible friendships
        random.shuffle(possible_friendships)
        # Create friendships for the first X pairs of the list
        # X is determined by the formula: num_users * avg_friendships // 2
        # Need to divide by 2 since each add_friendship() creates 2 friendships
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        q = Queue()
        q.enqueue([user_id])

        while q.size() > 0:
            path = q.dequeue()
            vertex = path[-1]
            if vertex not in visited:
                visited[vertex] = path
                for friend in self.friendships[vertex]:
                    new_path = path.copy()
                    new_path.append(friend)
                    q.enqueue(new_path)
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    # sg.populate_graph(10, 2)
    # print(sg.users)
    # print(sg.users[1])
    # connections = sg.get_all_social_paths(1)
    # print(connections)
    sg.add_user(1)
    sg.add_user(2)
    sg.add_user(3)
    sg.add_user(4)
    sg.add_user(5)
    sg.add_user(6)
    sg.add_user(7)
    sg.add_user(8)
    sg.add_user(9)
    sg.add_user(10)
    sg.add_friendship(1, 8)
    sg.add_friendship(1, 10)
    sg.add_friendship(1, 5)
    sg.add_friendship(2, 10)
    sg.add_friendship(2, 5)
    sg.add_friendship(2, 7)
    sg.add_friendship(3, 4)
    sg.add_friendship(4, 9)
    sg.add_friendship(5, 8)
    sg.add_friendship(6, 10)
    sg.add_friendship(8, 6)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)