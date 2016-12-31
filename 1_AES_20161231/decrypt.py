from Crypto.Cipher import AES
import base64

key = '00000000000000000000000000000000'
IV = '0000000000000000'
mode = AES.MODE_CBC

ciphertext = "49LiQFZExrkrWvxt4F90XA=="
print ciphertext

decryptor = AES.new(key, mode, IV=IV)
plaintext = decryptor.decrypt(base64.b64decode(ciphertext))

print plaintext
