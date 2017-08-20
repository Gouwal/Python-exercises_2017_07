# random 4 different numbers - 02
# -*- coding: utf-8 -*-
import random
guess_number = []
list = [i for i in range(10)]
print ("Original list =", list)

# compare above out put style,

for i in range(4):
    print (("i = %s") % i)

    j = random.randint(0, len(list) - 1)
    print (("j = %s") % j)

    guess_number.append(list[j])
    print(("list['j' = %s] = %s ") % (j, list[j]))
    print("guess_number = %s " % guess_number)

# you may can optimize above output code.

    print(("list.pop('j' = %s) = %s") % (j,list.pop(j)))
##    list.pop(j)
# It very import to cancel above code, because list.pop(j) already excute in code "print.....
    print(("list after pop ['j' = %s]) = %s") % (j, list))
    print ("*"*10)

    print ("*"*20)

print(f'method 2 (list): guess_number = {guess_number}')
print (len(list)-1)
print (list.pop(j))

# you can guess why abve list.pop(j) = 7?

print (guess_number[1:3])
