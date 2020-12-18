#!/usr/bin/env python3
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP as ciphersuite

file_enc = open("collection.bin", "rb")
private_key = RSA.import_key(open("private.pem").read())
cipher_rsa = ciphersuite.new(private_key)
plaintext = cipher_rsa.decrypt(file_enc.read())
print(plaintext)
