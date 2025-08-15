'''
if 
if-else
if - elif - else
'''


'''
    Syntax:

    if(condition):
        body
'''
# if(a > b):
#     print("a > b")
    
# # Indentation
# if (a >9):
#     print('asdjas')
#     print("dnask")
    
# if -else
a = 8
b = 9

if(a > b): 
    print("if block", a)
else:
    print("else block", b)
    
# If - elif -else

age = 15

if(age >= 18):
    print("Allowed")
elif(age >= 16 and age < 18):
    print("Allowed with parent")
else:
    print("Not Allowed")