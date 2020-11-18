import random

print('-------------------------------')
print('      GUESS THAT NUMBER')
print('-------------------------------')
print()

the_number = random.randint(0 , 100)
guess = -1

while guess != the_number:
    guess_text = input('guess a number between 0 and 100 :')
    guess = int(guess_text)

    if guess < the_number:
        print('too low')
    elif guess > the_number:
        print('too high')
    else:
        print('you win')

print('done!')
