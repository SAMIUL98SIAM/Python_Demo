'''number = '0,123,siam,45,617,90,89'
for i in range(0,len(number)):
    #print(number[i])
    if number[i] in '0123456789':
        print(number[i])
print(len(number))
states = ['navada','california','texas','washington','chicago']
for state in states:
    print('Name of state is: ',state.upper())'''
for i in range(1,13):
    for j in range(1,5):
        print('{1} Times {0} is {2}'.format(i,j,i*j))
    print('-----------------')
    print('-----------------')