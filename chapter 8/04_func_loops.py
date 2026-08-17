# def table(number):
#     number = int(input("Enter number:"))
#     for i in range(1, 11):
#         print(number * i)

# table(5)



# def calculate_total(numbers):
#     total = 0
#     for number in numbers:
#         total += number

#     return total
# result = calculate_total([10, 20, 40 ,7])
# print(result)



# def count_even(numbers):
#     count = 0
#     for number in numbers:
#         if number %2 == 0:
#             count += 1
#     return count

# print(count_even([10, 6, 7, 89, 2, 56, 2]))




def count_positive(numbers):
    count = 0
    for number in numbers:
        if number > 0:
            count += 1
    return count

print(count_positive([10, -1, 90, -56, -3, -6]))












