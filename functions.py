# def greet_user(first_name,last_name):
#     print(f'Hi {first_name}{last_name}!')
#     print('Welcome')
#
#
# print("Start")
# greet_user(f irst_name="Rahul ",last_name="Patel")
try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(age)
    print(risk)
except ZeroDivisionError:
    print('Age is not to be 0.')
except ValueError:
    print("Invalid Value")