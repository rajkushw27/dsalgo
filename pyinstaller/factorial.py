number = int(input("Please Enter a Positive Integer: "))

factorial = 1

if number < 0:
    print("Negative Number factorial is not defined")

if number == 0:
    print(f'factorial of {number} is {1}')

else:
    for i in range(1, number+1):
        factorial = factorial*i

    print(f'factorial of {number} is {factorial}')

wait = input()

# Sample Command
# pyinstaller --onefile ./factorial.py
