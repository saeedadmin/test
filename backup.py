Check for performance issues and rewrite the code:
import random as rnd
import os
import keyboard

print ('welcome to my game please inter two number which i guess between that numbers')
try:
    a = input('a = add number : ')
    b = input('b = add number bigger than a :')
    counter = input('counter = How many time i can guess : ')
    ready = input('if you are ready pleas inter y if not inter n : ')
except KeyboardInterrupt:
    print ("\nunexpected key press")
    exit()

def reload(msg):
        print(msg,"\n")
        os.system(f"python {'game.py'}")

def typechek(arg):
    for element in arg:
        type_arg = type(element)
    if type_arg != int:
        reload("you must inter numerical try again")
    else:
        continue

def ext(msg):
    print (msg)
    exit()

arycheck = [a,b,counter]
typechek(arycheck)

if int(a) >= int(b):
    reload ("a must be smaller than b try again")

if ready != 'y':
    ext('when you ready back and play')

shomaresh = int(counter) + 1
while ready == 'y':
    hads = rnd.randint(int(a),int(b))
    shomaresh -= 1
    if shomaresh == 0:
        print('I tried ',counter,'times and I lose!!!')
        break
    print('hads man : ',hads)
    print('I have ',shomaresh - 1,'chance')
    rahnema = input('hads man dorost bud?(b=>big, s=>small, t=true) ')
    if rahnema == 'b':
        b = hads - 1
    elif rahnema == 's':
        a = hads + 1
    else:
       print ('I tried ', shomaresh + 1,'times and I win your number is : ', hads)
       break    