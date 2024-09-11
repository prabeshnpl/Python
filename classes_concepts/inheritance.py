class User():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(self.name)

    def rank(self):
        return print(f'{self.name} is at rank : Gold')


class Archer(User):
    def __init__(self, name,age):
        User.__init__(self,name,age)

    def power(self):
        print(f'User {self.name}\nArcher\'s power left: 25 arrows\n')


class Wizard(User):
    def power(self):
        print(f'User {self.name}\nWizard\'s power left: 80% mana\n')


class Wizardcher(Archer, Wizard):
    def __init__(self, name, age):
        User.__init__(self,name, age)
    
    def power(self):
        Wizard.power(self)
        Archer.power(self)



player1 = Wizard('Prabesh', 18)
player1.power()

player2 = Archer('Prasamsha',11)
player2.power()
print(player2.name+'\n')

player3 = Wizardcher('Tika', 50)
player3.power()
