from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('--test1', help='test', default=100)
parser.add_argument('--test2', help='test')
args = parser.parse_args()
print(args)
