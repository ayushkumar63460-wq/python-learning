'''Write a recursive function to calculate the sum of first n natural numbers'''
def cal_sum(n):
    if n == 0:
        return 0
    return n + cal_sum(n-1)

print(cal_sum(5))