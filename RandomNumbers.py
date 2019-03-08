import random

#Create a reandom integer between 0 and 10
randNum = random.randint(0,10)

#real random number
readlRand = random.random()

#random choice out of a funky range
funkyRange = random.randrange(0,10,7)

#Printing a random number
print(f'A random number between 0 and 10 is {randNum}')
print(f'A real random number between 0 and 10 is {readlRand}')
print(f'This is a funky random number {funkyRange}')