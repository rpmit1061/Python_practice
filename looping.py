command = ""
started = False

while True:
    command = input(">>")
    if command.lower() == "start":
        if started:
            print("Car is already Started")
        else:
            started = True
            print("Car is started")
    elif command.lower() == "stop":
        if not started:
            print("Car is already Stoped")
        else:
            started = False
            print("Car is stoped")
    elif command.lower() == "help":
        print("""
                For Start car Type start.
                For Stop Stop car type stop
        """)
    elif command.lower() == "quit":
        break
    else:
        print("I don't Understand what do you want.")

secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int (input('Guess :'))
    guess_count +=1
    if guess == secret_number:
        print('You won')
        break
    else:
        print('Sorry you failed')
# Car Code


# For Loop
prices = [10,20,30]
total = 0
for price in prices:
    total +=price
print (f"Total : {total}")

for i in range (4):
    for j in range(4):
        print(f'({i},{j})')

number = [5,4,3,2,2]
for x_count in number:
    print('x' * x_count)
    output = ""
    for count in range(x_count):
        output += 'x'
    print(output)
numbers = [3,5,7,10,8]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)
# 2-D list
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix[0][1])
for row in matrix:
    for item in row:
        print(item)
numbers = [5,6,8,8,5,2]
uniqe = []
for number in numbers:
    if number not in uniqe:
        uniqe.append(number)
print(uniqe)