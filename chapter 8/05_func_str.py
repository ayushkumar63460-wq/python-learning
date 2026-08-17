'''Count how many vowels are in a string.'''
def count_vowel(text):
    count = 0
    for char in text:
        if char in "aeiou":
            count += 1
    return count

print(count_vowel("Terry the Terrible"))


