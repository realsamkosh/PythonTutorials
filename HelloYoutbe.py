# import math
# pi = 3.14
# print(round(pi))
# print(math.ceil(pi))

# name = "Sam Akosh"
# first_name = name[3:]
# print(first_name)

# while True:
#     name = input('What is your name')
#     if name != "":
#         break

# phone_number = "123-456-7890"
# for i in phone_number:
#     if i == "-":
#         continue
#     print(i,end="")

# tuple = collection which is ordered
#        and unchangeable used to group together related data
# student = ("Badejo Daniel",12,"male")
# print(student.index("male"))
# print(student.count("male"))

# for x in student:
#     print(x)
#
# if "Badejo Daniel" in student:
#     print("Badejo is Here")
# str1 = "python"
# str2 = str1[:2] + str1[2:]
# print(str1[:2])
# print(str2)
# print(str1 in 2*str2)
# stopped at sets

def solve(a, b):
    return b if a == 0 else solve(b % a, a)


print(solve(20, 50))
