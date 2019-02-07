class Animal:
    BREED_TIME = 0
    def __init__(self, x, y):
        self.breedCounter = self.BREED_TIME
        self.location = (x,y)

    def move(self):
        pass

    def reproduce(self):
        if self.breedCounter == 0:
            pass
        pass


class Prey (Animal):
    BREED_TIME = 6
    LOCATION_MARKER = "p"
    def __init__(self, x, y):
        super().__init__(x, y)

class Predator (Animal):
    STARVE_TIME = 8
    BREED_TIME = 8
    LOCATION_MARKER = "P"

    def __init__(self, x, y):
        super.__init__(x, y)
        self.starvecounter = self.STARVE_TIME


    def eat(self):
        pass

    def die(self):
        pass



class Island:
    ISLAND_SIZE = 10

    def __init__(self):
        self.grid = [['0' for i in range(Island.ISLAND_SIZE)] for i in range(Island.ISLAND_SIZE)]

    def griddisplay(self):
        for row in self.grid:
            print(row)


def main():
    animallist = []
    islanda = Island()


    animallist.append(Prey(1,2))
    print(animallist[0].breedCounter)
    islanda.grid[animallist[0].location[0]][animallist[0].location[1]] = "p"
    islanda.griddisplay()


if __name__ == '__main__':
    main()