# Simple coin toss guessing game. The player gets two guesses
# However, the program has several bugs in it. Run a few times and find the bugs that keep it from working correctly.

# This is the program with the bugs like in the book:
# import random
# guess = ''
# while guess not in ('heads', 'tails'):
#     guess = input()
# toss = random.randint(0,1) # 0 is tails, 1 is heads
# if toss == guess:
#     print('You got it!')
# else:
#     print('Nope! Guess again!')
#     guesss = input()
#     if toss == guess:
#         print('You got it!')
#     else:
#         print('Nope. You are really bad at this game.')



# This is the program without bugs and working correctly:
import random, logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

logging.debug('Start of the program')
guess = ''
heads = 1
tails = 0
while guess not in (heads, tails):
    print('Guess a number between 0 and 1!')
    guess = int(input())
    if guess == 1 or guess == 0:
        break
toss = random.randint(0,1) # 0 is tails, 1 is heads
if toss == int(guess):
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = int(input())
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
logging.debug('End of the program')