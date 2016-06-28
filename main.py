from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Hash import SHA256
import distance, bitarray, binascii

def hamming2(s1, s2):
    """Calculate the Hamming distance between two bit strings"""
    assert len(s1) == len(s2)
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))

class Ticket:
    seedTicket = 0
    nroSequencia = 0

    def __init__ (self,seedTicket, nroSequencia):
        self.seedTicket = seedTicket
        self.nroSequencia = nroSequencia
    #
    # def __str__(self):
    #     return nroSequencia + ", " + seedTicket

    def __repr__(self):
        return "Ticket: %s, %s" % (self.nroSequencia, self.seedTicket)

nroTickets = 0
nroSequencia = 0
i = 0
ticketsVendidos = []
iv = Random.get_random_bytes(16)
ba1 = bitarray.bitarray()
ba1 = bitarray.bitarray()
plainTextDelay = ""
parametroDelay = 3000000


nroTickets = input("Quantos tickets vendidos? ")
print ("Gerando tickets...")
for i in range (0,nroTickets):
    nroSequencia = nroSequencia + 1
    seed = Random.get_random_bytes(16)
    ticketsVendidos.append(Ticket(seed, nroSequencia))
#print ticketsVendidos

print "Gerando o hash..."
hashTicket = SHA256.new()
for i in range (nroTickets-10,nroTickets):
    hashAtual = hashTicket.digest() + ticketsVendidos[i].seedTicket
    hashTicket.update(hashAtual)
print hashTicket.digest()
#base 58 check/ ripem 160/ hat/ etherum
chave = hashTicket.digest()
ciphertext = chave

print "Delay Function..."
tamanhoMensagem = 16*parametroDelay

for i in range (0,tamanhoMensagem):
    plainTextDelay = plainTextDelay + "0"

obj = AES.new(chave, AES.MODE_OFB, iv)
ciphertext = obj.encrypt (plainTextDelay)
ciphertext = ciphertext[len(ciphertext)-32:]

print ciphertext
print "---------------"

ciphertext = str(bin(int(binascii.hexlify(ciphertext),16)))
ciphertext = ciphertext[2:]
faltaCipher = 256 - len(ciphertext)
if faltaCipher != 0:
    for i in range(0,faltaCipher):
        ciphertext = "0" + ciphertext
print ciphertext

menorDistancia = 257
vencedor = 0
arrayVencedor = []
for i in range (0,nroTickets):
    hashTicket.update(ticketsVendidos[i].seedTicket)
    winningParameter = str(bin(int(binascii.hexlify(hashTicket.digest()),16)))
    winningParameter = winningParameter[2:]
    faltaCipher = 256 - len(winningParameter)
    if faltaCipher != 0:
        for i in range(0,faltaCipher):
            winningParameter = "0" + winningParameter
    distancia = hamming2(ciphertext, winningParameter)
    if distancia == menorDistancia:
        arrayVencedor.append("achei")
    if distancia < menorDistancia:
        arrayVencedor = []
        arrayVencedor.append("achei")
        menorDistancia = distancia
        vencedor = ticketsVendidos[i].nroSequencia


print "Distancia: " + str(menorDistancia)
print "Vencedor: " + str(vencedor)
print arrayVencedor
