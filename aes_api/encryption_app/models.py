from django.db import models

# class Test(object):
#     def hello(self):
#         return "Hello World"

# For AESExecutor
import json
from collections import namedtuple
class AESExecutor(object):
    """
    JSON format:
    {
        "key":"my name is varun",
        "mode":"e/d",
        "values":[
            "str1","str2"
        ]
    }
    """
    def execute(self,json_data):
        self.json_obj = json.loads(json_data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
        aes = AESCipher(self.json_obj.key)
        if self.json_obj.mode == "e":
            function = aes.encrypt
        elif self.json_obj.mode == "d":
            function = aes.decrypt
        else:
            return "Mode error -- Ensure mode is one of <e/d>"
        self.res = []
        for val in self.json_obj.values:
            if(self.json_obj.mode == "e"):
                self.res.append(aes.encrypt(val))
            elif(self.json_obj.mode == "d"):
                self.res.append(aes.decrypt(val))
        return self.to_json()
    
    def to_json(self):
        first = True
        json_str="{"
        for index,res in enumerate(self.res):
            if(first):
                first = False
            else:
                json_str += ","
            # Ensure res is string
            try: 
                res = res.decode("utf-8")
            except AttributeError:
                pass
            json_str += "\"" + self.json_obj.values[index] + "\":\"" +  res +"\""
        json_str += "}"
        return json_str


# For AES Cipher
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
