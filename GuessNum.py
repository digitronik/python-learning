import random
secretnum = random.randint(1,20)
print('I m thinking of the number between 1 to 20')
for guesstaken in range(1,7):
    print('take a guess')
    guess = int(input())
    if guess < secretnum:
        print('your guess is too low')
    elif guess > secretnum:
        print ('your guess is too high')
    else:
        break
if guess == secretnum:
    print ('good job ' + str(guesstaken)+'!')
else:
    print('nope the number i was thinking of was '+ str(secretnum))
        