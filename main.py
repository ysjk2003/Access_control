import argparse
from auth_check.auth_check import *

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", help="url option")
    parser.add_argument("-t", "--txt", help="add txt file option")
    parser.add_argument("-k", "--keyword", help="keyword")


    args = parser.parse_args()
    access_control = auth_check()

    if args.url and args.txt and args.keyword:
        target = access_control.load_targets(args.txt)
        access_control.auth_check(args.url, target, args.keyword)
    else:
        print("Usage : -u URL -t TXTFILE -k KEYWORD")
        print("Type --help to show option list")