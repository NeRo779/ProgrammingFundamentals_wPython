sorting_hat = input()
while sorting_hat != 'Welcome!':
    name = len(sorting_hat)
    if sorting_hat == 'Voldemort':
        print(f'You must not speak of that name!')
        break
    elif name < 5:
        print(f'{sorting_hat} goes to Gryffindor.')
        sorting_hat = input()
        continue
    elif name == 5:
        print(f'{sorting_hat} goes to Slytherin.')
        sorting_hat = input()
        continue
    elif name == 6:
        print(f'{sorting_hat} goes to Ravenclaw.')
        sorting_hat = input()
        continue
    elif name > 6:
        print(f'{sorting_hat} goes to Hufflepuff.')
        sorting_hat = input()
        continue
if sorting_hat == 'Voldemort':
    print('')
else:
    print('Welcome to Hogwarts.')

