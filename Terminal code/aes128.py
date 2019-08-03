"""
AES-128 encryption/decrpytion
"""
import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES

class AESCipher(object):
    def __init__(self, key): 
        self.bs = 16
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]

key = input("\nEnter 16 Byte key:")
aes = AESCipher(key)

choice = input("\nEncrypt or Decrypt? (e/d):")
loop = True
while(loop):
    if choice == 'e':
        e = aes.encrypt(input("\nEnter plain text to encrypt:\n"))
        print("\nThe encrypted version in base 64 is:\n\n",e,"\n\n")
    else:
        print("\nThe plain text is: \n\n",aes.decrypt(input("\nEnter text to be Decrypted {input would be in base 64}:\n")),"\n\n")
    proceed = input("Do you want to continue? [Y/n]:")
    loop = False if (proceed == 'n' or proceed == 'N') else True
