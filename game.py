import random

def get_input(prompt, type_func):
    while True:
        try:
            user_input = type_func(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input. Please try again.")

def main():
    print('Welcome to my game. Please enter two numbers between which I will guess.')
    a = get_input('a = add number: ', int)
    b = get_input('b = add number bigger than a: ', int)
    if a >= b:
        print("a must be smaller than b. Please try again.")
        return
    counter = get_input('counter = How many times I can guess: ', int)
    ready = input('If you are ready, please enter y. If not, enter n: ')
    if ready != 'y':
        print('When you are ready, come back and play.')
        return
    shomaresh = counter + 1
    while ready == 'y':
        hads = random.randint(a, b)
        shomaresh -= 1
        if shomaresh == 0:
            print('I tried', counter, 'times and I lose!!!')
            break
        print('My guess:', hads)
        print('I have', shomaresh - 1, 'chances left.')
        rahnema = input('Was my guess correct? (b => big, s => small, t => true): ')
        if rahnema == 'b':
            b = hads - 1
        elif rahnema == 's':
            a = hads + 1
        else:
            print('I tried', shomaresh + 1, 'times and I win. Your number is:', hads)
            break

if __name__ == '__main__':
    main()