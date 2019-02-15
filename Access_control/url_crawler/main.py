import argparse
from crawler.url_crawler import *

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", help="ex) 192.168.1.1")
    parser.add_argument("-p", "--port", help="port option")

    args = parser.parse_args()

    if args.port and args.url:
        port = "tcp port " + args.port + " and host " + args.url
        sniffing(port)
    else:
        print("Usage : -u URL -p PORT")
        print("Type --help to show option list")