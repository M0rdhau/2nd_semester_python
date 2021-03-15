#Diffie-Hellman key exchange

def genKey (pub1, priv, pub2):
    return (pub1**priv)%pub2

#Public keys
P = 971
G = 977
#Alice
a = 42
#Bob
b = 68

print("Public and private keys are: Bob - " + str(P) + " and " + str(a) + "; Alice - " + str(G) + " and " + str(b) + "\n")

aliceown = genKey(G,a,P)
bobown = genKey(G,b,P)

print("Generated keys are: Bob - " + str(bobown) + "; Alice - " + str(aliceown) + "\n")

commonalice = genKey(bobown, a, P)
commonbob = genKey(aliceown, b, P)

print("Common secrets are: Bob - " + str(commonbob) + "; Alice - " + str(commonalice))