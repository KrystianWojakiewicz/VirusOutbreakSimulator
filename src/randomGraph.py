import src.graph as graph
import random as r


class RandomGraph(graph.Graph):
    def __init__(self, number_of_vertices, avg_number_of_friends):
        super().__init__(number_of_vertices)
        self.generate_random_graph(number_of_vertices, avg_number_of_friends)

    def create_edge_or_not(self, prob, frm, to):
        """ Simulate a coin toss and create an edge between frm->to based on the specified probability
        :param prob: probability with which we are simulating the coin toss
        :param frm: "from" node
        :param to: "to" node
        """
        if self.is_edge(frm, to):
            pass

        if r.random() <= prob:
            self.add_edge(frm, to)

    @staticmethod
    def calculate_probability(number_of_vertices, avg_number_of_friends):
        """
        Generate a probability between [0,1] based on the desired number of average friends
        The number 2 is needed, because when we create an edge, we have two nodes engaged, so we the probability
        needs to be halved to make up for that.
        """
        return avg_number_of_friends / (2 * number_of_vertices)

    def generate_random_graph(self, number_of_vertices, avg_number_of_friends):
        """Create an empty graph and fill it with random edges."""
        probability_of_edge = self.calculate_probability(number_of_vertices, avg_number_of_friends)

        for vertex in range(number_of_vertices):
            for potential_edge in range(1, number_of_vertices):
                self.create_edge_or_not(probability_of_edge, vertex, potential_edge)
        return self

    def calculate_average_friends(self):
        """Helper function to be removed after tests or moved to somewhere else.
        Calculate the average number of friends for a node in the graph.
        """
        total = 0
        for vertex in self._vert_dict.values():
            total += len(vertex.get_connections())
        mean = total / self.get_num_vertices()
        return mean
