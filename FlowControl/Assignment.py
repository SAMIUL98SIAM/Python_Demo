credit = 3

number_of_course = int(input('Number of courses: '))
if number_of_course==1:
    mark = int(input("Enter the marks 1: "))
    if mark>=80 and  mark<=100:
        GPA = 4
    elif mark>=70 and  mark<=79:
        GPA = 3.8
    elif mark>=40 and mark<=69:
        GPA = 2.5
    else:
        GPA = 0.00
    CGPA = GPA*credit/credit
    print(CGPA)
    if CGPA < 2.5: print("Fail")

elif number_of_course==2:
    mark = int(input("Enter the marks 1: "))

    if (mark>=80 and  mark<=100):
        GPA = 4

    elif (mark>=70 and  mark<=79):
        GPA = 3.8
        GPA1 = 3.8
    elif (mark>=40 and  mark<=69):
        GPA = 2.5

    else:
        GPA = 0.00


    mark2 = int(input("Enter the marks 2: "))

    if (mark2 >= 80 and mark2 <= 100):
        GPA1 = 4
    elif (mark2 >= 70 and mark2 <= 79):
        GPA1 = 3.8
    elif (mark2 >= 40 and mark2 <= 69):
        GPA1 = 2.5
    else:
        GPA1 = 0.00

    CGPA1 = (GPA*credit+GPA1*credit)/(credit+credit)
    if CGPA1<2.5:print("Fail")
    print(CGPA1)