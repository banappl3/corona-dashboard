import math

message = int(input("Enter the message to be encrypted: ")) 

p = int(input("Enter a prime number: ")) 
q = int(input("Enter an other prime number: "))
e = 3
n = p*q
 
def encrypt(me):
    """ Encrypt a message using predetermined prime number. """
    en = math.pow(me,e)
    c = en % n
    print("Encrypted Message is: ", c)
    return c
 
print("Original Message is: ", message)
c = encrypt(message)