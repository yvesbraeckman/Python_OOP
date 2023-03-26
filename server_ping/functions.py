import json
import platform
import subprocess
import sys


def main():
    if len(sys.argv) != 1:
        pass
    else:
        opperating_mode = int(input("1 voor tests, 2 voor lijst sites, 3 voor add or delete, 0 voor einde: "))
        fileObject = open("sites.json", "r")
        jsonContent = fileObject.read()
        sites = json.loads(jsonContent)
        while opperating_mode != 0:
            if opperating_mode == 1:  # pings sites in list
                for diction in sites:
                    print(myping(diction["adress"]))
            elif opperating_mode == 2:  # shows sites in list
                print(sites)
            elif opperating_mode == 3:  # add or delete site
                new_site = input("name: ")
                new_adress = input("adress: ")
                delete = False
                index = 0
                for i in range(len(sites)):
                    if new_adress == sites[i]["adress"]:
                        delete = True
                        index = i
                if delete:
                    del sites[index]
                if not delete:
                    sites.append({"name": new_site, "adress": new_adress})
                print(sites)
            else:
                print("geen geldige opperating mode")
            opperating_mode = int(input("1 voor tests, 2 voor lijst sites, 3 voor add or delete, 0 voor einde: "))
        jsonString = json.dumps(sites)
        jsonFile = open("sites.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
    return None


def myping(host):
    parameter = '-n' if platform.system().lower() == 'windows' else '-c'

    command = ['ping', parameter, '1', host]
    response = subprocess.call(command)

    if response == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    main()
