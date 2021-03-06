#!/usr/bin/python3

# Optixal

# Encrypt ASCII plaintext
# Using AES-CBC PKCS#7
# with provided 256-bit key
# and random 128-bit (16-byte) IV

import sys, codecs
from Crypto.Cipher import AES
from Crypto import Random

template = "{0:20}: {1:}"

def checkreq():
    if len(sys.argv) != 3:
        print("Usage:", sys.argv[0], "[plaintext file]", "[key file (hex)]")
        sys.exit(1)

def unhexify(s):
    return codecs.decode(s, 'hex')

def main():
    checkreq()
    
    # Read and Convert Key
    keyhex = open(sys.argv[2], 'r').read().strip()
    key = unhexify(keyhex)
    iv = Random.new().read(16)

    # Read, Convert and Pad Plaintext File
    plaintext = open(sys.argv[1], 'rb').read()
    pad_len = 16 - (len(plaintext) % 16)
    plaintext += bytes([pad_len]) * pad_len

    # Encrypt
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(plaintext)

    # Write Ciphertext Bytes to Output File
    with open(sys.argv[1] + '.enc', 'wb') as f:
        f.write(iv + ciphertext)

if __name__ == "__main__":
    main()
