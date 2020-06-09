from binascii import b2a_hex, a2b_hex

from Crypto.Cipher import AES


class AESEncrypt:
    def __init__(self):
        self.mode = AES.MODE_CBC

    def set_key(self, key):
        self.key_len = len(key)
        if not self.key_len == 16:
            raise Exception('密钥长度应为 16 Bytes')
        self.key = key

    def encrypt(self, text):
        # 被加密的明文长度必须是key长度的整数倍,如果不够,则用\0进行填充
        # 转成16进制字符串,是因为避免不可见的ascii在显示的时候捣乱
        cryptor = AES.new(self.key, self.mode, self.key)
        count = len(text)
        add = self.key_len - (count % self.key_len)
        text = text + ('\0' * add)
        cipher_text = cryptor.encrypt(str.encode(text, 'utf-8'))
        return b2a_hex(cipher_text)

    def decrypt(self, text):
        # 解密后需注意,加密时有可能填充\0,因此要去掉右侧的\0
        cryptor = AES.new(self.key, self.mode, self.key)
        plain_text = cryptor.decrypt(a2b_hex(text))
        return bytes.decode(plain_text.rstrip(b'\0'), 'utf-8')


# 单例
c = AESEncrypt()


# 设置AES中的密钥
def init(key):
    c.set_key(key)
    return c


# 加密
def encode(data):
    return c.encrypt(data)


# 解密
def decode(data):
    return c.decrypt(data)
