from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

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
# world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']

reverse = {
    'n': 's',
    's': 'n',
    'w': 'e',
    'e': 'w'
}

traversal_path = []
#order 1 lookup
visited = {}
#pathing, where did we come from -> where to go next?
move = []

#takes away from use case that there is no previous in beginning node
visited[player.current_room.id] = player.current_room.get_exits()

#we want to stop when we have visited every node in the graph
while len(visited) != len(room_graph) - 1:  

    #if yet to visit, set in visited 
    if player.current_room.id not in visited:
        # get list of exits to edit them to know which way we have gone before
        visited[player.current_room.id] = player.current_room.get_exits()
        prev = move[-1]
        #remove the way we have just come from as an open path
        visited[player.current_room.id].remove(prev)

    #if we have traveled here before, and there are no open ways to go besides somewhere we've been before, go back until there is an open way
    while len(visited[player.current_room.id]) == 0:
        prev = move.pop()
        #don't wanna pop twice, hold that specific node
        traversal_path.append(prev)
        player.travel(prev)

    #travels based on first given opening
    nxt = visited[player.current_room.id].pop(0)
    traversal_path.append(nxt)
    move.append(reverse[nxt])
    player.travel(nxt)



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
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
