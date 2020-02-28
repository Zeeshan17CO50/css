import math

def prime(num):
    for i in range(2, num//2): 
        if (num % i) == 0: 
            return False
    else: 
        return True 


def compute_e():
        for e in range(2,phi_n):
                if (math.gcd(e,phi_n)==1) and (e !=p) and (e !=q):
                        return e


def compute_d(e):
        i = 0
        while True: 
                if ((i * e) % phi_n) ==1:
                        return i
                i += 1

def cipher_text(message,e,n):
        c=[(ord(i)**e) % n for i in message]
        return c

def decript_text(ct,d,n):
        decript=[chr((i**d) % n) for i in ct]
        return decript

p, q = map(int, input("Enter the two numbers: ").split(','))
message = input("Enter the value of m: ")
n = p * q
phi_n = (p-1)*(q-1)
print(f'n: {n}\nphi(n): {phi_n}')

if prime(p) and prime(q):
        e = compute_e()
        d = compute_d(e)          
        ct=cipher_text(message,e,n)
        dt=decript_text(ct,d,n)     
# for i in message:
#         i = ord(i)
#         if prime(p) and prime(q):
#                 e = compute_e()
#                 d = compute_d(e)   
#         #  print(compute_d(e_value))
        # cipher_text=[(ord(char)**e) % n for char in message]
        # decript_text=[chr((char**d) % n) for char in cipher_text]
print("e: ",e)
print("Cipher Text: ",ct)
#print(''.join(map(lambda x: str(x), cipher_text)))
print("Decript Text: ",dt)

