#Class Inheritance

class User():
    def sign_in(self):
        print('logged in')

class Wizard(User): #--> here we can see that class Wizard inherits from class User
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows: left- {self.num_arrows}')



wizard1 = Wizard('Merlin', 50)
wizard1.sign_in()
archer1 = Archer('Robin', 100)
archer1.sign_in()
wizard1.attack()
archer1.attack()


#introspection

print(dir(wizard1))