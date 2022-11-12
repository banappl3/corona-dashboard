import math

def is_prime(num):
    """Returns True if the number is prime
    else False."""
    if num == 0 or num == 1:
        return False
    for x in range(2, num):
        if num % x == 0:
            return False
    else:
        return True

def primes(n): # simple sieve of multiples 
   odds = range(3, n+1, 2)
   sieve = set(sum([list(range(q*q, n+1, q+q)) for q in odds], []))
   return [2] + [p for p in odds if p not in sieve]

def teilerfremd(a,b):
    t= 2
    erg=True
    while t<=min(a,b):
        if (a%t==0 and b%t==0):
            erg=False
            break
        t=t+1
    return erg

def e_calculate(phi):
    e=0
    for f in range(2,phi):
        if teilerfremd(f,phi):
            e=f
            break
        else:
            continue
    return e

def extgcd(a,b):
    """Determine the parameter of the equation: gcd(a,b)=ua+bv """
    u, v, s, t = 1, 0, 0, 1
    while b!=0:
        q=a//b
        a, b = b, a-q*b
        u, s = s, u-q*s
        v, t = t, v-q*t
    return a, u, v

def modinverse(a, b,n):
    """Calculate the modular multiplicative inverse over the extended Euclidean algorithm."""
    a, u, v=extgcd(a, b)
    return u%n

def encrypt(me,e,n):
    """ Encrypt a message using predetermined prime number. """
    en = math.pow(me,e)
    c = en % n
    print("Encrypted Message is: ", c)
    return c

def decrypt(cipher, d, n):
    dec= modpot(cipher,d,n) # Fast modular exponentiation
    print("Decrypted Message is: ", str(dec))
    return dec
    
def modpot(x, y, m):
    """Fast modular exponentiation"""
    pot = 1
    while y > 0:
        if y % 2 == 1:
            pot = (pot * x) % m
            y = y - 1
        else:
            x = (x * x) % m
            y = y // 2
    return pot

def main(rsa_modul):
    num=rsa_modul
    p = max(primes(num))
    q = primes(num)[-2]
    n=p*q
    phi=(p-1)*(q-1)
    e=e_calculate(phi)
    d = pow(e, -1, phi) # a simply way to calculate the modular multiplicative inverse

    message = int(input("Enter the message to be encrypted: ")) 
    print("The first prime number is "+str(p))
    print("The other prime number is "+str(q))
    print("Original Message is: ", message)
    c = encrypt(message,e,n)
    rsa_message = decrypt(c,d,n)
    if message==rsa_message:
        print("The messages are equal.")

main(50)