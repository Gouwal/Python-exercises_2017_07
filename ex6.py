x = "There are %d types of people." % 10 # take the sentance to x, and show 10 in the sentance
binary = "binary"
do_not = "don't"
y = "Those who know %s and thoes who %s." % (binary, do_not) #格式化字符放入两个变量

print x
print y

print "I said: %r." %x #变量名为x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious #打印出joke_evaluation所赋字符串以及变量名hiarious变量名所赋的False.

w = "This is the left side of..." #字符串赋予w
e = "a string with a right side." #字符串赋予e

print w+e