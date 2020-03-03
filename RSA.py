'''
Created on Feb 24, 2020

@author: ccoew
'''

p = input("Enter value of p:")
q =input("Enter value of q:")
mes = input("Enter message:")

def computeGCD(x, y): 
    while(y): 
        x, y = y, x % y 
    return x 

def findn(x,y):
    return x*y

def findEulerQuotient(x,y):
    return (x-1)*(y-1)

def finde(euler):
    for i in range(2,euler):
        if computeGCD(euler,i) == 1:
            return i

def findd(euler,e):
    for i in range(1,euler):
        if (i*e)%(euler)==1:
            return i        
        
def encrypt(message,e,n):
    return((message**e)%n)

def decrypt(message,d,n):
    return ((message**d)%n)

n = findn(p, q)
euler = findEulerQuotient(p, q)
e =finde(euler)
d = findd(euler, e)
print "private key:",(e,n) 
print "private key:",(d,n)
cipher = encrypt(mes, e, n)
print "Encrypted Text:",cipher
normal = decrypt(cipher, d, n)
print "Decrypted Text:",normal


'''
Enter value of p:11
Enter value of q:3
Enter message:7
private key: (3, 33)
private key: (7, 33)
Encrypted Text: 13
Decrypted Text: 7
'''