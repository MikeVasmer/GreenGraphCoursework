#!/usr/bin/env python

from argparse import ArgumentParser
from matplotlib import pyplot as plt
from graph import Greengraph

def process():
    parser = ArgumentParser(
        description="Produce graph of green land between two locations")
    parser.add_argument("--start", required=True,
                        help="The starting location ")
    parser.add_argument("--end",  required=True,
                        help="The ending location")
    parser.add_argument("--steps",  required=True,
                        help="The number of steps between the starting and ending locations")
    parser.add_argument("--out",  required=True,
                        help="The output filename")
    arguments = parser.parse_args()

    mygraph = Greengraph(arguments.start, arguments.end)
    data = mygraph.green_between(arguments.steps)
    plt.plot(data)
    # TODO add a title and axis labels to this graph
    plt.savefig(arguments.out)

if __name__ == "__main__":
    process()
