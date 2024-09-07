import random
class TooHigh(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class TooLow(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

number=random.randint(0,100)
while True:
    try:
        data = int(input('Guess the number: '))
        if data > number:
            raise TooHigh('Please Enter Lower Number!')
        elif data < number:
            raise TooLow('Please Enter Higher Number!')
        else:
            print('Correct')
            break
    except (TooHigh, TooLow,ValueError) as e:
        print(e)

