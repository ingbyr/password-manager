from Crypto.Cipher import AES

# 单例模式
__encoder = None
__decoder = None


def init_encoder(key):
    global __encoder
    __encoder = AES.new(key, AES.MODE_EAX)
    return __encoder.nonce


def init_decoder(key, nonce):
    global __decoder
    __decoder = AES.new(key, AES.MODE_EAX, nonce)


def encode(data):
    return __encoder.encrypt(str.encode(data, 'utf-8'))


def decode(encrypted_data):
    return bytes.decode(__decoder.decrypt(encrypted_data), 'utf-8')
