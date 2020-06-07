from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


# AES加密
class Encrypt:

    def __init__(self, key, nonce=None):
        self.password_key = key
        if nonce:
            self.cipher = AES.new(self.password_key, AES.MODE_EAX, nonce=nonce)
        else:
            self.cipher = AES.new(key, AES.MODE_EAX)
        self.nonce = self.cipher.nonce

    def encode(self, data):
        return self.cipher.encrypt(str.encode(data, 'utf-8'))

    def decode(self, encrypted_data):
        return bytes.decode(self.cipher.decrypt(encrypted_data), 'utf-8')


instance = None


# 设置密钥
def init(key):
    global instance
    instance = Encrypt(key)
    return instance.nonce


# 设置密钥
def init(key, nonce=None):
    global instance
    if nonce:
        instance = Encrypt(key, nonce)
    else:
        instance = Encrypt(key)
    return instance.nonce


if __name__ == '__main__':
    en = init(get_random_bytes(16))
    print(en.decode(en.encode(b'2sdfvaerb')))
    print(en.decode(en.encode(b'3')))
    print(en.decode(en.encode(b'3sdf')))
    print(en.decode(en.encode(b'3sadfff')))
