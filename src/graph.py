class Vertex:
    def __init__(self, node):
        self._id = node
        self._adjacent = {}

    def __str__(self):
        return str(self._id) + ' adjacent: ' + str([x.get_id() for x in self._adjacent])

    def add_neighbor(self, neighbor, weight=0):
        self._adjacent[neighbor] = weight

    def get_connections(self):
        return self._adjacent.keys()

    def get_id(self):
        return self._id

    def get_weight(self, neighbor):
        return self._adjacent[neighbor]


class Graph:
    def __init__(self):
        self._vert_dict = {}
        self._num_vertices = 0

    def __init__(self, number_of_vertices):
        self._vert_dict = {}
        self._num_vertices = 0
        for vertex in range(number_of_vertices):
            self.add_vertex(vertex)

    def __iter__(self):
        return iter(self._vert_dict.values())

    def get_num_vertices(self):
        return self._num_vertices

    def add_vertex(self, node):
        self._num_vertices = self._num_vertices + 1
        new_vertex = Vertex(node)
        self._vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self._vert_dict:
            return self._vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost=0):
        if frm not in self._vert_dict:
            self.add_vertex(frm)
        if to not in self._vert_dict:
            self.add_vertex(to)

        self._vert_dict[frm].add_neighbor(self._vert_dict[to], cost)
        self._vert_dict[to].add_neighbor(self._vert_dict[frm], cost)

    def get_vertices(self):
        return self._vert_dict.keys()

    def is_edge(self, frm, to):
        for vertex in self._vert_dict[frm].get_connections():
            if vertex.get_id() == to:
                return True
        for vertex in self._vert_dict[to].get_connections():
            if vertex.get_id() == frm:
                return True
        return False

    def print_graph(self):
        for vertex in self._vert_dict.values():
            print(vertex)
