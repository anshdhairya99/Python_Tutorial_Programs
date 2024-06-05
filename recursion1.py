# Recursion In Python:-----------------

def print2(str1):
    print("This is " + str1)
print2("harry")

# Iterative Method:------👇
# n! = n * n-1 * n-2 * n-3.......1
# n! = n * (n-1)!

#def factorial_iterative(n):
#     """
#     :param n: Integer
#     :return: n * n-1 * n-2 *n-3.......1
#     """
#     fac = 1
#     for i in range(n):
#         fac = fac * (i+1)
#     return fac
# number = int(input("Enter the number"))

# print("factorial using Iterative Method",factorial_iterative(number))

# Recursive Method :--👇

# n! = n * n-1 * n-2 * n-3.......1
# n! = n * (n-1)!
def factorial_recursive(n):
    """
    :param n: Integer
    :return: n * n-1 * n-2 *n-3.......1
    """
    if n ==1:
        return 1
    else:
        return n * factorial_recursive(n-1)
number = int(input("Enter the number"))
print("Factorial using iterative method",factorial_recursive(number))
print("Factorial using recursive Method",factorial_recursive(number))

