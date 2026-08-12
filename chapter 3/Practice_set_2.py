letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''
print(letter.replace("<|Name|>","Ayush").replace("<|Date|>",("25/02/2030")))   #.replace string function helped here