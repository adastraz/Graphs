from util import Queue
class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('Vertex does not exist')

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def earliest_ancestor(self, ancestors, starting_node):
        q = Queue()
        q.enqueue([starting_node])

        visited = set()
        traveled = []

        while q.size() > 0:
            path = q.dequeue()
            vertex = path[-1]

            if vertex not in visited:
                visited.add(vertex)

            for neighbor in self.get_neighbors(vertex):
                new_path = list(path)
                new_path.append(neighbor)
                q.enqueue(new_path)
                traveled.append(new_path[-1])

            if traveled == []:
                return -1
        print(traveled)
        return traveled[-1]


if __name__ == '__main__':
    g = Graph()  
    g.add_vertex(1)
    g.add_vertex(2)
    g.add_vertex(3)
    g.add_vertex(4)
    g.add_vertex(5)
    g.add_vertex(6)
    g.add_vertex(7)
    g.add_vertex(8)
    g.add_vertex(9)
    g.add_vertex(10)
    g.add_vertex(11)

    g.add_edge(1, 10)
    g.add_edge(3, 1)
    g.add_edge(3, 2)
    g.add_edge(5, 4)
    g.add_edge(6, 3)
    g.add_edge(6, 5)
    g.add_edge(7, 5)
    g.add_edge(8, 4)
    g.add_edge(8, 11)
    g.add_edge(9, 8)

    test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(g.vertices)
print(g.earliest_ancestor(test_ancestors, 1))
print(g.earliest_ancestor(test_ancestors, 2))
print(g.earliest_ancestor(test_ancestors, 3))
print(g.earliest_ancestor(test_ancestors, 4))
print(g.earliest_ancestor(test_ancestors, 5))
print(g.earliest_ancestor(test_ancestors, 6))
print(g.earliest_ancestor(test_ancestors, 7))
print(g.earliest_ancestor(test_ancestors, 8))
print(g.earliest_ancestor(test_ancestors, 9))
print(g.earliest_ancestor(test_ancestors, 10))
print(g.earliest_ancestor(test_ancestors, 11))