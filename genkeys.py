#!/usr/bin/env python3
from Crypto.PublicKey import RSA

key = RSA.generate(2048)
file = open("private.pem", "wb")
file.write(key.exportKey('PEM'))
file.close()

publickey = key.publickey()
file = open("public.pem", "wb")
file.write(publickey.exportKey('PEM'))
file.close()
