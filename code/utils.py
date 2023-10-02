from argparse import ArgumentParser


def get_arguments():
    parser = ArgumentParser()
    parser.add_argument("--contacts")

    args = parser.parse_args()
    return args
