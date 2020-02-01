class Parrot:
    def fly(self):
        print("Parrot can fly")
    def swim(self):
        print("Parrot can't swim")

class Penguin:
    def fly(self):
        print("Penguin can't fly")
    def swim(self):
        print("Penguin can swim")

def flying_test(bird):
    bird.fly()

pa = Parrot()
peng = Penguin()

flying_test(pa)
flying_test(peng)