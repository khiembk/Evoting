import random
import sys
import elgamal
keys = elgamal.generate_keys()
priv = keys['privateKey']
pub = keys['publicKey']
PRIMENO = priv.p
generator = priv.g

secretVal = priv.x

X = pow(generator, secretVal,PRIMENO)
y = random.randint(1, PRIMENO)
Y = pow(generator, y,PRIMENO)

print("P (the Prover) generates these values:")
print("secretVal(secret)= ", secretVal)
print("PRIMENO= ", PRIMENO)
print("h = ", X)

print("\nP generates a random value (r):")
print("r =", y)

print("P computes a = generator^r (mod PRIMENO) and passes to V:")

print("a =", Y)

print("V generates a random value (e) and passes to P:")

c = random.randint(1, PRIMENO)
print("e =", c)
print("P calculates z = r + secretVal*e (mod PRIMENO) and send to V (the Verifier):")

z = (y + c * secretVal)

print("z=", z)

print("V now computes val=generator^z (mod PRIMENO) and (a h^e (mod PRIMENO)) and determines if they are the same\primeNo")

val1 = pow(generator, z,PRIMENO)
val2 = (Y * pow(X,c,PRIMENO)) % PRIMENO

print("val1= ", val1, end=' ')
print(" val2= ", val2)

if (val1 == val2):
    print("P has proven that P knows secretVal")
else:
    print("Failure to prove")