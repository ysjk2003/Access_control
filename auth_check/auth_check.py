import requests

class auth_check:
    def load_targets(self, filename):
        try:
            target_file = open(filename, "r")
        except FileNotFoundError as exception:
            print(filename + "Not Found")
            return False
        else:
            file_string = target_file.read().split("\n\n")
        target_file.close()

        get = []
        post = []
        put = []
        delete = []

        print("Loding TXT File ...")
        for area in file_string:
            line = area.split("\n")
            if line[0].upper() == "GET:":
                get = line[1:]
            elif line[0].upper() == "POST:":
                post = line[1:]
            elif line[0].upper() == "PUT:":
                put = line[1:]
            elif line[0].upper() == "DELETE:":
                delete = line[1:]
            else:
                print("Unexpected Tag :" + line[0])
                return False

        targets = [get, post, put, delete]
        print("target File Loading Complete!")
        return targets

    def auth_check(self, url, target, key):
        log_file = open("./auth_check.log", 'w')
        print("Starting Page Authentication Check ...")
        for index, method in enumerate(target):
            for target in method:
                uri = url + target
                print("Checking " + uri + " ...")
                req = None
                if index == 0:
                    req = requests.get(uri)
                elif index == 1:
                    req = requests.post(uri)
                elif index == 2:
                    req = requests.put(uri)
                elif index == 3:
                    req = requests.delete(uri)
                if req.text.find(key) == -1:
                    log_file.write(uri + " Redirect not detected\n")
                else:
                    log_file.write(uri + " redirect detect\n")

        print("Finish! Let's see log!")
        log_file.close()
