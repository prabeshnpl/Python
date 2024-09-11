class math():
    PI = 3.14

    
    @staticmethod
    def add(num1, num2):
        return print(f'The sum of {num1} and {num2} is {num2+num1}')

    def sub(num1, num2):
        return print(f'The difference of {num1} and {num2} is {num1-num2}')
    
    def non_static():
        return print("This is not static or class method")


    @classmethod
    def multiply(cls, num1, num2):
        return print(f'Product is {num1*num2}')


class PlayerCharacters():
    membership = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def fire(self):
        return f'{self.name} is ready to fire'

    @classmethod
    def initialize(cls, name, age):
        return cls(name, age)


playerone = PlayerCharacters('Prabesh', 20)
print(playerone.fire())

playertwo = PlayerCharacters.initialize('Prabesh', 4)
print(playertwo.age)

math.add(4, 5)
math.sub(5, 4)
math.multiply(4, 3)

print(math.PI)

math.non_static()

rule = math()
rule.multiply(4, 5)
