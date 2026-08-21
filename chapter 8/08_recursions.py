'''A function calls itself to solve a smaller version of the same problem.'''

def countdown(n):
    if (n == 0):
        return
    print(n)
    countdown(n-1)

countdown(9)
'''Every recursive funtions needs a base case like here n== 0 to stop at 1,
which says STOP we are done otherwise error beacuse goes on forever.'''


def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(5))