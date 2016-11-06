import random



secret_num = 5
guesses_left = 5
play = True


print

while play:
    guess = int(raw_input('What is the number?'))
    guesses_left -= 1
    if guess == secret_num:
        print 'Goo job.'
        break
    elif guess > secret_num:
        print '%d is too big' % (guess)
    else:
        print '%d is too low.' % (guess)
    if guesses_left == 0:
        print 'Youran out of guesses'
        break
play_again = raw_input('Do you want to play again?(Y or N)').upper()

if play_again == 'N':
    play == False
else:
    pass
