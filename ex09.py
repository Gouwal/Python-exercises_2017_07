# random 4 differernt numbers-01

import random
guess_number = []

list = [i for i in range(10)]
guess_number = random.sample(list, 4)

# for test
print (guess_number)

while guess_number[0] == 0:
    guess_number = random.sample(list, 4)

# for test
    print("new_guess_number", guess_number)

print (f'method 1(random.sample): guess_number = {guess_number}')
# for test different print code
print (guess_number)
