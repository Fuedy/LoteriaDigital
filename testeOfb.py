from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Hash import SHA256
import distance, bitarray, binascii

iv = Random.get_random_bytes(16)
chave = Random.get_random_bytes(16)
mensagem = ""
parametroDelay = 3000000

tamanhoMensagem = 16*parametroDelay

mensagem = "0"*tamanhoMensagem

obj = AES.new(chave, AES.MODE_OFB, iv)
ciphertext = obj.encrypt (mensagem)
#print mensagem
print ciphertext
#obj2 = AES.new(chave, AES.MODE_OFB, iv)
#resposta = obj2.decrypt(ciphertext)
#print resposta
print "---------------"
