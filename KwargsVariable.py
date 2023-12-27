# **kwargs = parameter that will pack all arguments into a dictionary
#            useful so that a function can accept a varying amount of keyword argument


def hello(**parm):
    # print("Hello " + parm["last"] + " " + parm["first"])
    for key, value in parm.items():
        print(value, end=" ")


hello(last="Akosile", first="Samuel")
