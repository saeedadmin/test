arycheck = [a,b,counter]

def typechek(arg):
    for element in arg:
        type_arg = type(element)
    if type_arg != int:
        reload("you must inter numerical try again")
    else:
        continue
    
typechek(arycheck)