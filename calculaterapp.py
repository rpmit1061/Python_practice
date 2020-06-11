import re

print("Megical Calculater")
print("Type quit to Exit")

previous = 0
run = True

def performMath():
    global run
    global previous
    equation = ""
    if previous == 0:
        equation = input("Input Equation: ")
    else:
        equation = input(str(previous))

    if equation == "quit":
        print("Good Bye")
        run = False
    else:
        equation = re.sub('[a-zA-z,.:() " "]','',equation)

        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)


while run:
    performMath()