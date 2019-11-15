from Pacman import *
import os.path

def place(words):
    arg = words[1].split(',')
    pm = Pacman(int(arg[0]), int(arg[1]), str(arg[2]))
    return pm

def report(pm):
    print("{},{},{}".format(pm.x, pm.y, pm.f))

def main():

    filename = input("Please enter command file: ")

    # checks if file exists
    while (not os.path.isfile(filename)):
        filename = input("Invalid file name, please re-enter: ")

    with open(filename, "r") as f:
        for line in f:
            # removes all trailing whitespaces, and turns all letters into uppercase
            line = line.strip().upper()
            words = line.split()

            if (words != []):
                try:
                    if (words[0] == "PLACE"):
                        pm = place(words)

                    elif (words[0] == "LEFT"):
                        pm.update(-1)

                    elif (words[0] == "RIGHT"):
                        pm.update(1)

                    elif (words[0] == "MOVE"):
                        pm.move()

                    elif (words[0] == "REPORT"):
                        report(pm)
                        break

                except:
                    pass


if __name__ == "__main__":
    main()
