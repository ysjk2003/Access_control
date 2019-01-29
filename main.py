import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", help="url option")
    parser.add_argument("-t", "--txt", help="add txt file option")
    parser.add_argument("-r", "--redirect", help="redirect url")


    args = parser.parse_args()

    if args.url and args.txt and args.redirect:
        auth_check.load_targets(args.txt)
        auth_check.auth_check(args.url, args.txt, args.redirect)
    else:
        print("Usage : -u URL -t TXTFILE -r REDIRCTURL")
        print("Type --help to show option list")