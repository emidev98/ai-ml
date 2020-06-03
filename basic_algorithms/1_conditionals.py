nameUser1 = input('Insert your name user 1 : ')
ageUser1 = int(input(f'{nameUser1} insert your age: '))

nameUser2 = input('Insert your name user 2 : ')
ageUser2 = int(input(f'{nameUser2} insert your age: '))

if ageUser1 < ageUser2:
    print(f'{nameUser1} is younger than {nameUser2}')
elif ageUser1 > ageUser2:
    print(f'{nameUser2} is younger than {nameUser1}')
else:
    print(f'{nameUser1} and {nameUser2} are in the same age')