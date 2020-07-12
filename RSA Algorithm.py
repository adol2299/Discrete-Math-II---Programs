try:
   input = raw_input
except NameError:
   pass
try:
   chr = unichr
except NameError:
   pass

 # Ingreso de números primos p y q #
p=int(input('Ingrese el número primo p: '))
q=int(input('Ingrese el número primo q: '))
print("Los números primos escogidos son:\np=" + str(p) + ", q=" + str(q) + "\n")

 # Cálculo de n=p*q #
n=p*q
print("n = p * q = " + str(n) + "\n")

 # Cálculo de phi de Euler #
phi=(p-1)*(q-1)
print("La función phi de Euler [phi(n)]: " + str(phi) + "\n")

 # Cálculo del máximo común divisor usando el algoritmo de Euclides #    
def  gcd(a, b):
    if (b == 0):
        return a
    else:
        return gcd(b, a % b)

 # Cálculo del módulo inverso #
def modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

 #Cálculo de los números coprimos con Phi(n), además se ingresan en el arreglo l#    
def coprimes(a):
    l = []
    for x in range(2, a):
        if gcd(a, x) == 1 and modinv(x,phi) != None:
            l.append(x)
    for x in l:
        if x == modinv(x,phi):
            l.remove(x)
    return l

 # Impresión de los números coprimos con phi(n) y elección del coprimo e #   
print("Escoja un e de los números coprimos mostrados abajo:\n")
print(str(coprimes(phi)) + "\n")
e=int(input())

# Cálculo del exponente de la clave privada d e impesión de las llaves #
d=modinv(e,phi)
print("\n Su clave pública es el par de números (e=" + str(e) + ", n=" + str(n) + ").\n")
print("Su clave privada es el par de números (d=" + str(d) + ", n=" + str(n) + ").\n")

# Bloques de encriptación y desencriptación con sus respectivas funciones # 
def encrypt_block(m):
    c = modinv(m**e, n)
    if c == None: print('No existe inverso multiplicativo modular para el bloque  ' + str(m) + '.')
    return c
def decrypt_block(c):
    m = modinv(c**d, n)
    if m == None: print('No existe inverso multiplicativo modular para el bloque  ' + str(c) + '.')
    return m
def encrypt_string(s):
    return ''.join([chr(encrypt_block(ord(x))) for x in list(s)])
def decrypt_string(s):
    return ''.join([chr(decrypt_block(ord(x))) for x in list(s)])

 # Impresión del mensaje original, encriptado y desencriptado al finalizar el programa #    
s = input("Ingrese el mensaje a encriptar: ")
print("\nMensaje original: " + s + "\n")
enc = encrypt_string(s)
print("Mensaje encriptado: " + enc + "\n")
dec = decrypt_string(enc)
print("Mensaje desencriptado: " + dec + "\n")