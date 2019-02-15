import argparse
import requests

def session(url, data):
    headers = {'Content-Type' : 'application/json'}
    response = requests.post(url, headers=headers, data=data)
    return response.cookies.get_dict()

def logout(logouturl, sess):
    cookie = sess
    response = requests.get(logouturl, cookies=cookie)
    print(response.cookies.get_dict())

def login(url, sess):
    response = requests.get(url=url, cookies=sess)
    return response.cookies.get_dict()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", '--url', help="http://www.example.com/login")
    parser.add_argument("-d", "--data", help="input json")
    parser.add_argument("-l", "--logouturl", help="http://www.example.com/logout")
    args = parser.parse_args()

    if args.url and args.data and args.logouturl:
        sess = session(args.url, args.data)
        logout(args.logouturl, sess)
        login(args.url, sess)
    else:
        print("Usage : -u URL")
        print("Type --help to show option list")