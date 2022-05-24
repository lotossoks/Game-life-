import random, os, time

w_l = int(input())
conf = []
Continue = True


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def printWorld(world):
    for i in range(w_l):
        print(*world[i])


def newWorld(world):
    nW = [["_" for j in range(w_l)] for i in range(w_l)]
    for i in range(w_l):
        for j in range(w_l):
            C = world[i][j]
            lon = [
                world[i % (w_l - 1) - 1][j % (w_l - 1) - 1],
                world[i % (w_l - 1) - 1][j % (w_l - 1) + 0],
                world[i % (w_l - 1) - 1][j % (w_l - 1) + 1],
                world[i % (w_l - 1) + 0][j % (w_l - 1) - 1],
                world[i % (w_l - 1) + 0][j % (w_l - 1) + 1],
                world[i % (w_l - 1) + 1][j % (w_l - 1) - 1],
                world[i % (w_l - 1) + 1][j % (w_l - 1) + 0],
                world[i % (w_l - 1) + 1][j % (w_l - 1) + 1]
            ]
            alive = lon.count("X")
            if C == "X":
                if alive == 2 or alive == 3:
                    nW[i][j] = "X"
            elif C == "_":
                if alive == 3:
                    nW[i][j] = "X"
    return (nW)


world = [[random.choice(["X", "_"]) for j in range(w_l)] for i in range(w_l)]
while Continue:
    cls()
    printWorld(world)
    conf.append(world.copy())
    world = newWorld(world)
    time.sleep(0.25)
    Continue = not world in conf
print("Finish!")
