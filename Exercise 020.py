import random
stu1 = str(input("Enter name 1: "))
stu2 = str(input("Enter name 2: "))
stu3 = str(input("Enter name 2: "))
stu4 = str(input("Enter name 4: "))
list = [stu1, stu2, stu3, stu4]
random.shuffle(list)
print("Name of student is {}".format(list))
