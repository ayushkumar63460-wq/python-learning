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
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(5))


'''def function(n):

    if stopping_condition:
        return

    # do some work

    function(smaller_problem)'''




'''SUM OF NUMBERS'''
def sum_num(n):
    if n == 0:
        return 0
    return n + sum_num(n-1)

print(sum_num(5))


'''COUNTING WITH RECURSION'''
def count_digit(n):
    if n == 0:
        return 0
    return 1 + count_digit(n // 10)    
print(count_digit(8999))


'''POWER RECURSION'''
def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)
print(power(2, 3))
    

'''RECURSION WITH STRINGS'''
def reverse(text):
    if len(text) <= 1:
        return text
    return reverse(text[1:]) + text[0]

print(reverse("Making"))


'''RECURSION WITH LISTS'''
def list_num(numbers):
    if len(numbers) == 0:
        return 0
    return numbers[0] + list_num(numbers[1:])
print(list_num([10, 20, 30, 40]))


'''FIBONACCI'''
def fibonaci(n):
    if n == 0:
        return 0

    if n == 1:
        return 1
    return fibonaci(n-1) + fibonaci(n-2)
print(fibonaci(5))


'''1. Write the first call.
2. Keep expanding recursive calls.
3. Stop at the base case.
4. Start returning upward.
5. Substitute returned values.'''


'''count vowels recursively'''
def count_vow(text):
    if text == "":
        return 0
    if text[0] in "aeiou":
        return 1 + count_vow(text[1:])
    return count_vow(text[1:])

print(count_vow("Making"))