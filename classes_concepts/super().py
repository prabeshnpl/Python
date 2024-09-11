class User():
    def __init__(self, name,age,role):
        self.name=name
        self.age=age
        self.role = role

    def Role(self):
        return print(f'You are {self.role}\n')


class Archer(User):
    def __init__(self, name,age):
        super().__init__(name,age,'Archer')

    def power(self):
        print(f'User {self.name}\nArcher\'s power left: 25 arrows\n')


player1 = Archer('Prasamsha',11)
player1.Role()
print(player1.age)
player1.power()
