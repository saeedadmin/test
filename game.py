import random

def get_input(prompt, type_func):
    while True:
        try:
            user_input = type_func(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input. Please read the descripton try again ")
        except KeyboardInterrupt:
            print("ok bye bye bye")
            exit()
        except Exception as e:
            print("unknown keyboard", e)
def main():
    print('Welcome to my game. Please enter two numbers which I will guess.',"\n\n guide: \n 1)give me two numbers number a bigger than number b\n\n 2)if you don't want to give me numbers skeep that i will use the a = 0 and b = 100 and count = 4\n\n 3)ctrl+c => exit()\n\n")
    a = get_input('a = add number: ', int)
    b = get_input('b = add number bigger than a: ', int)
    if a + 1 >= b:
        print("a must be smaller than b. Please try again.")
        return
    counter = get_input('counter = How many times I can guess: ', int) or 4
    ready = get_input('If you are ready, please enter y. If not, enter n: ',str)
    if ready != 'y':
        print('When you are ready, come back and play.')
        return
    shomaresh = counter + 1
    while ready == 'y':
        hads = random.randint(a = 0, b = 100)
        shomaresh -= 1
        if shomaresh == 0:
            print('I tried', counter, 'times and I lose!!!')
            break
        print('My guess:', hads)
        print('I have', shomaresh - 1, 'chances left.')
        rahnema = get_input('Was my guess correct? (b => big, s => small, t => true): ',str)
        if rahnema == 'b':
            b = hads - 1
        elif rahnema == 's':
            a = hads + 1
        elif rahnema == 't':
            print('I tried', shomaresh + 1, 'times and I win. Your number is:', hads)
            break
        else:
            break

if __name__ == '__main__':
    main()