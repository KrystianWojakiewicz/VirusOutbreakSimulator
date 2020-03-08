import src.graph as graph
import random as r


def get_random_integer():
    r.seed()
    return r.random() * 100


def create_edge_or_not(gr, prob, frm, to):
    if gr.is_edge(frm, to):
        pass

    r_int = get_random_integer()
    if r_int < prob:
        gr.add_edge(frm, to)


def generate_random_graph(number_of_vertices):
    gr = graph.Graph(number_of_vertices)
    probability_of_edge = 50

    for vertex in range(number_of_vertices):
        for potential_edge in range(1, number_of_vertices):
            create_edge_or_not(gr, probability_of_edge, vertex, potential_edge)
    return gr


def main():
    n = 10
    gr = generate_random_graph(n)
    gr.print_graph()


if __name__ == '__main__':
    main()
