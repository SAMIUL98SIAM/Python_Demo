print(
    """January: {2}
       February: {0}
       March:  {2}
       April: {1}
       May:   {2}
       June:  {1}
       July: {2}
       August: {2}
       September: {1}
       October: {2}
       November: {1}
       December: {2}   
    """.format(28,30,31)
)

for i in  range(1,12,2):
    print('No. %2d squared is %4d and qubed is %4d'%(i,i**2,i**3))
print()
for i in range(1, 12, 1):
    if(i%2==1):
        print('No. {}  squared is   {} and qubed is   {:4}'.format(i, i ** 2, i ** 3))
