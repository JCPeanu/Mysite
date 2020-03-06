
import random
def guess():
    x = random.randint(0,100)
    while True:
        try:
            a = int(input('guess:'))
            print('a:', a)
            if a > x:
                print('too large')
            elif a < x:
                print('too small')
            else:
                print("GOOD JOB!")
                break
        except:
            print("Wrong input, please input again.")
guess()