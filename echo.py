import argparse
parser = argparse.ArgumentParser()
parser.add_argument("message", help="Message to be echoed")
parser.add_argument("-c", "--capitalize", action="store_true")
args = parser.parse_args()
if args.capitalize:
    print(args.message.capitalize())
else:
    print(args.message())