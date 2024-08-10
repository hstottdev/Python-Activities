import random

def printValueAndType(value):
    print("The number is ", value , ' the type is ',type(value))

randomNumber1 = random.randint(1,100)
randomNumber2 = random.randrange(100,10000)/100
randomNumber3 = complex(random.randint(1,100),random.randint(1,100))



printValueAndType(randomNumber1)
printValueAndType(randomNumber2)
printValueAndType(randomNumber3)
