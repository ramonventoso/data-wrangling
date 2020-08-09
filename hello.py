import random
import sys  

print (sys.version)
print (sys.executable)

print('Hello, what is your name?')
name = input()

secretNumber = random.randint(1, 20)

print('Well ' + name + ', I am thinking in a number between 1 and 20')


for i in range(1, 7):
    print('Take a guess')
    guess = int(input())
    if guess < secretNumber:
        print('Your guess is too low')
    elif guess > secretNumber:
        print('Your guess is too high')
    else:
        break

if guess == secretNumber:
    print('You got it ' + name + ' in ' + str(i) + ' times')
else:
    print('Nope!. I was thinking in ' + str(secretNumber))




