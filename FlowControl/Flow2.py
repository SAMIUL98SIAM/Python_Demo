parrot = 'Norwegian Blue'
letter = input("Enter the char: ")
if letter not in parrot:
    print('{0} these letter didnt contain in "{1}" words'.format(letter,parrot))
else:
    if (letter.upper()=='i') or (letter.upper() == 'a') or (letter.upper() == 'e') or (letter.upper() == 'o') or (letter.upper()=='u'):
        print('Gimme an {0} Bob'.format(letter))
    elif (not letter.upper()=='i') or (not letter.upper() == 'a') or (not letter.upper() == 'e') or (not letter.upper() == 'o') or (not letter.upper()=='u'):
        print('Gimme a {0} Bob'.format(letter))

