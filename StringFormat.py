# str.format() = optional method that gives users
# more control when displaying output


number = 1000

print("The pi value is  {:.3f}".format(number))
print("The number is  {:,}".format(number))
print("The number is  {:b}".format(number))
print("The number is  {:o}".format(number))
print("The number is  {:X}".format(number))
print("The number is  {:E}".format(number))
# animal = "cow"
# item = "moon"
# print("The "+animal+" jumped over the "+ item)
# print("The {} jumped over the {}".format(animal,item))
# print("The {1} jumped over the {0}".format(animal,item)) # positional argument
# print("The {animal} jumped over the {item}".format(animal="cow",item="moon")) # keyword argument

# name = "Samuel Akosile"
# print("Hello, My name is {}".format(name))
# print("Hello, My name is {:30}".format(name))
# print("Hello, My name is {:20}. Nice to meet you".format(name))
# print("Hello, My name is {:>20}. Nice to meet you".format(name))
# print("Hello, My name is {:<20}. Nice to meet you".format(name))
# print("Hello, My name is {:^20}. Nice to meet you".format(name))