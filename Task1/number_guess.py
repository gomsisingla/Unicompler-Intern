import random
t = 0
g = int(input("Total Guesses: "))
print('Guess no. b/w 1-100')
x = random.randint(1, 100)
n = int(input("Enter an integer between the given range: "))
 
while (x != 'n'):
    if(t<(g-1)):
        if n < x:
            print("The number guessed is low")
            t = t+1
            n = int(input("Enter an integer between the given range: "))
        elif (n > x):
            print("The number guessed is high")
            t = t+1
            n = int(input("Enter an integer between the given range: "))
        else:
            print("The number guessed is right")
            print("Total guesses taken: ", t+1)
            break
    else:
        print("Ran out of tries! \nYou loose the Game!")
        break
