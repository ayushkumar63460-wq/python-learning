'''Write a python function to print first n lines of the following pattern.'''
def star_pattern(n):
    if n == 0:
        return
    print("*" * n)
    star_pattern(n-1)

star_pattern(3)
