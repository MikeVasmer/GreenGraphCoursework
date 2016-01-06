from argparse import ArgumentParser
from matplotlib import pyplot as plt
from graph import Greengraph

def process():
    parser = ArgumentParser(
        description="Produce graph quantifying the amount of green land between two locations")
    parser.add_argument("--start", required=True, nargs="+",
                        help="The starting location ")
    parser.add_argument("--end",  required=True, nargs="+",
                        help="The ending location")
    parser.add_argument("--steps", type=int,
                        help="An integer number of steps between the starting and ending locations, defaults to 10")
    parser.add_argument("--out",
                        help="The output filename, defaults to graph.png")
    arguments = parser.parse_args()

    mygraph = Greengraph(arguments.start, arguments.end)
    if arguments.steps:
        data = mygraph.green_between(arguments.steps)
    else:
        data = mygraph.green_between(10)
    plt.plot(data)
    plt.xlabel("Step")
    plt.ylabel("Greenness")
    plt.title("Graph of green land between " + " ".join(arguments.start) + " and " + " ".join(arguments.end))
    if arguments.out:
        plt.savefig(arguments.out)
    else:
        plt.savefig("graph.png")

if __name__ == "__main__":
    process()
