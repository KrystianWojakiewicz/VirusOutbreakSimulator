import src.randomGraph as rGraph


def main():
    """Main entry point for the program."""
    n = 1000
    avg_number_of_friends = 3
    gr = rGraph.RandomGraph(n, avg_number_of_friends)
    gr.print_graph()
    print('mean: ' + str(gr.calculate_average_friends()))


if __name__ == '__main__':
    main()
