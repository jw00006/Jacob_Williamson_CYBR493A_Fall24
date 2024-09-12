"""
Python Introduction
9/12/24
Jake W
"""

def printVariableInfo():
    '''
    simple function prints out types of local variables
    :return:
    '''
    # comment
x=5
print(type(x))
y=3.1
print(type(y))
z=0

print(printVariableInfo())

name="abcde"
print(type(name))
name2='edcbe'
print(type(name2))

ips = ["192.168.10.1", 10, "192.168.10.2","192.168.10.3","192.168.10.4","192.168.10.5",]
print(type(ips))
print(type(ips[0]))
print(ips[2]+ips[3])
for ip in ips:
    print (ip)

if(ips[1]<=20):
    print("value is less than than 20")
else:
    print('value is greater than 20')

def MethodThatAcceptsData(x, y, z):
    '''
    this method accepts three variables and returns their respective data types
    :param x:
    :param y:
    :param z:

    '''
print("x is ", type(x))
print("y is ", type(y))
print("z is ", type(z))

#methodThatAcceptsData(100, [0, 1, 2, 3, 4, 5], wvu)
#print var info
