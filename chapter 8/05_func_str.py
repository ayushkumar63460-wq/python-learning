'''Count how many vowels are in a string.'''
def count_vowel(text):
    count = 0
    for char in text:
        if char in "aeiou":
            count += 1
    return count

print(count_vowel("Terry the Terrible"))


def greet(name = "user"):
    print("Hello", name)

greet("Ayush")
'''Keyword arguments are useful when a function has several parameters and you want the call to be clear.'''



'''*args'''
def add(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print(add(10, 89, 79, 67))



'''*args   normal stuff
→ collect extra positional arguments
→ tuple

**kwargs  #name=...
→ collect extra keyword arguments
→ dictionary'''
