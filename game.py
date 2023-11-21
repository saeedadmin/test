import random

def get_input(prompt, type_func):
    while True:
        try:
            inter = input(prompt)
            if inter == "":
                return inter
            else:
                user_input = type_func(inter)
                return user_input
        except ValueError:
            print("Invalid input. Please read the description and try again")
        except KeyboardInterrupt:
            print("Ok bye bye bye")
            exit()
        except Exception as e:
            print("Unknown error:", e)

def main():
    print('Welcome to my game. Please enter two numbers which I will guess.\n\nGuide:\n1) Give me two numbers, number a bigger than number b.\n2) If you don\'t want to give me numbers, I will use a = 0, b = 100, and count = 4.\n3) Ctrl+C => exit()\n')
    a = get_input('a = add number: ', int)
    b = get_input('b = add number bigger than a: ', int)
    if a == "":
        a = 0 
    if b == "":    
        b = 100
    if a + 1 >= b:
        print("a must be smaller than b. Please try again.")
        return
    counter = get_input('counter = How many times I can guess: ', int)
    ready = get_input('If you are ready, please enter y. If not, enter n: ', str)
    if ready != 'y':
        print('When you are ready, come back and play.')
        return
    if counter == "":
        counter = 4
    shomaresh_count = counter + 1
    try:
        while ready == 'y':
            hads = random.randint(a, b)
            shomaresh_count -= 1
            if shomaresh_count == 0:
                print('I tried', counter, 'times and I lose!!!')
                break
            print('My guess:', hads)
            print('I have', shomaresh_count - 1, 'chances left.')
            rahnema = get_input('Was my guess correct? (b => big, s => small, t => true): ', str)
            if rahnema == 'b':
                b = hads - 1
            elif rahnema == 's':
                a = hads + 1
            elif rahnema == 't':
                print('I tried', shomaresh_count + 1, 'times and I win. Your number is:', hads)
                break
            else:
                break
    except Exception:
        print('hey something wrong happened i think i guess true and you lie to me')
        exit()
if __name__ == '__main__':
    main()