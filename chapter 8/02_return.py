def get_score():               
    print(100)

get_score()
score = get_score()
print(score) 

'''The function showed you 100 but it never gave 100 to score, it merely informed you of its existence..
BUT return FIXES THIS SHIT '''   

def get_score():
    return 100
score = get_score()
print(score)    
'''I get handed the 100 not just know that 100 is there and now i also can use that 100 anywhere i want...
print
↓
announcement 

return
↓
actual thing handed back '''





def square(n):
    return n * n
print(square(5)) 

def add(a, b):
    return (a+b)
result = add(10, 20)
if result > 10:
    print("Big")


