# TASK - 1


def fact_rec(number):
    if number == 1:
        return 1
    else:
        factorial = number * fact_rec(number - 1)
        return factorial

num = int(input("Enter a number: "))
print(f"Factorial of {num} is: {fact_rec(num)}")
