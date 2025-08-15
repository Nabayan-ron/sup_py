'''
    Strings:
'''

s = 'hi i am string'
s1 = "hello"

print(s, type(s))

# Accessing ELements in str
print(s1[0])
print(s1[-1])
print(s1[4])

'''
# String doesn't support this

s1[1] = 'x'
print(s1)
'''

# String Concatenation

s2 = s+ " "+s1
print(s2)

# String Slicing

sen = "mynameispython"
print(len(sen))
# syntax: str[start_index(default 0): end_index(excluded,default len(str)): steps(included, default 1)]

print(sen[0:8:1]) # mynameis
print(sen[:8]) # mynameis
print(sen[-6:]) # python
print(sen[:]) #sen[0:len(sen)] -> mynameispython


# Step slicing
print(sen[::2])
print(sen[-8::2]) # ipto



l = '''
    this 
    is 
    a
    string
'''

print(l)

'''
    not in
    in
'''

strrrr = 'heloo i am juju'

# l : str = 'jasdas'
print('heloo' not in strrrr)


# f -strings

x = 99
y = 11
res = x-y

print("x = ",x," y = ",y," res = ", x," - ", y," which is ",res)
print(f"x = {x}, y = {y}, res = {x} - {y} which is {res}")

# User input???

# inp = input("Give me a value:") # Default str
# print(type(inp),inp*2)

# typecasting

# imp = float(input("GIve me a value:"))
# print(type(imp), imp*2)


ty = "       i amm STR      "

print(ty.upper())
print(ty.lower())
print(ty.strip()) # Remove spaces from both ends

print('new line\nnew linme') # \n

print('sneha\'s \tbook')

print("hndasdjasdas \"jnkdasbndasndn\"")

lk = "hello, how are you?"

lk = lk.replace("hello", "shjadhjkas")
print(lk)