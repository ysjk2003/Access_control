import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", help="url option")
parser.add_argument("-t", "--txt", help="add txt file option")


args = parser.parse_args()

if args.url and args.txt:
    print(args.url, args.txt)
else:
    print("no")