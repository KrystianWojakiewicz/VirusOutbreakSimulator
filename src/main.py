import src.graph as graph
import random as r


def create_edge_or_not(gr, prob, frm, to):
    """ Simulate a coin toss and create an edge between frm->to based on the specified probability
    :param gr: the graph you are creating an edge for
    :param prob: probability with which we are simulating the coin toss
    :param frm: "from" node
    :param to: "to" node
    """
    if gr.is_edge(frm, to):
        pass

    if r.random() <= prob:
        gr.add_edge(frm, to)


def calculate_probability(number_of_vertices, avg_number_of_friends):
    """
    Generate a probability between [0,1] based on the desired number of average friends
    The number 2 is needed, because when we create an edge, we have two nodes engaged, so we the probability
    needs to be halved to make up for that.
    """
    return avg_number_of_friends/(2 * number_of_vertices)


def generate_random_graph(number_of_vertices, avg_number_of_friends):
    """Create an empty graph and fill it with random edges."""
    gr = graph.Graph(number_of_vertices)
    probability_of_edge = calculate_probability(number_of_vertices, avg_number_of_friends)

    for vertex in range(number_of_vertices):
        for potential_edge in range(1, number_of_vertices):
            create_edge_or_not(gr, probability_of_edge, vertex, potential_edge)
    return gr


def calculate_average_friends(gr):
    """Helper function to be removed after tests or moved to somewhere else.
    Calculate the average number of friends for a node in the graph.
    :param gr: graph to calculate the average for.
    """
    total = 0
    for vertex in gr._vert_dict.values():
        total += len(vertex.get_connections())
    mean = total / gr.get_num_vertices()
    return mean


def main():
    """Main entry point for the program."""
    n = 1000
    avg_number_of_friends = 3
    gr = generate_random_graph(n, avg_number_of_friends)
    gr.print_graph()
    print('mean: ' + str(calculate_average_friends(gr)))


if __name__ == '__main__':
    main()
