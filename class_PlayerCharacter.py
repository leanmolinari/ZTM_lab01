##Class Example

class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('run')

    def speack(self):
        print(f'my name is {self.name}, and I am {self.age} years old')


player1 = PlayerCharacter('Lean', 100)
player1.speack()