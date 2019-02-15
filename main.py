import argparse
from auth_check.auth_check import *
from crawler.url_crawler import *

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", help="url option")
    parser.add_argument("-t", "--txt", help="add txt file option")
    parser.add_argument("-k", "--keyword", help="keyword")
    parser.add_argument("-m", "--mode", help="select mode")
    parser.add_argument("-p", "--port", help="port")


    args = parser.parse_args()
    access_control = auth_check()

    if args.mode == 'auth_check':
        if args.url and args.txt and args.keyword:
            target = access_control.load_targets(args.txt)
            access_control.auth_check(args.url, target, args.keyword)
        else:
            print("Usage : -u URL -t TXTFILE -k KEYWORD")
            print("Type --help to show option list")
    elif args.mode == 'crawler':
        if args.port and args.url:
            port = "tcp port " + args.port + " and host " + args.url
            sniffing(port)
        else:
            print("Usage : -u URL -p PORT")
            print("Type --help to show option list")
    else:
        print("Usage : -m mode")
        print("Type --help to show option list")