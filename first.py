'''
    MultiLine
    comment
'''
"""
    This
    is
    also
    a 
    comment
"""
# Single line comment

print("Hi, I am print")
print('Hi, I am python')

'''
    1. High-level Lang
    2. Scripting Lang
    G.V Rosum
'''
'''
    Data Type:
    
    int 
    float
    bool
    str
    list -> array
    sets
    tuples
    dictionary
'''

a = True
print(a, type(a))

a : int = 10 #Declaration


'''
Operators:

1. Arithmatic:
    +
    -
    * 
    /
    // (floor division) 
    ** (power/exponential)
    % (ampersand)
2. Conditional
'''


a = 10
b = 20

print(a+b)
print(a-b)
print(a*b)
print(a/b)

# // (floor division) 10/8=> 1.2 -> 1
print(16//5) 
#Expo
print(3**2) # ->9
# power(base, exponent)
print(pow(3,2))


'''
Conditional:
    > greater than
    <
    <=
    >=
    = assignment
    == equality
    ! not 
    != not equal

    returns bool value (True/False)
'''

val = 10
value = 11

print(val == value)


'''
    Boolean operators: (0,1)
    AND     1,1 -> 1           0,1 -> 0           1,0 -> 0           0,0 ->0
    OR        1,1-> 1       0,1-> 1      1,0 -> 1     0,0 -> 0
    NOT         1-> 0       0->1
    
    XOR     0,1 -> 1      1,0 -> 1         1,1 -> 0          0,0->0 (Odd 1's detector)
    NOR (NOT(OR))
    NAND (NOT(AND))
'''
x = True
y =False
print(not((x and y) or (x or y)))

# print("or", or)


'''
    +=
    -=
    *=
    /=
'''

s = 11

s+= 7 # S = S+7
print(s)