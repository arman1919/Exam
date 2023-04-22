# File Encryption and Decryption


from Crypto.Cipher import AES


BLOCK_SIZE = 16
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)


unpad = lambda s: s[:-ord(s[len(s)-1:])]



def read_file(file_path):
    with open(file_path, 'rb') as f:
        return f.read()


def write_file(file_path, data):
    with open(file_path, 'wb') as f:
        f.write(data)


def encrypt_file(input_file_path, output_file_path, key):

    cipher = AES.new(key, AES.MODE_CBC)


    input_data = read_file(input_file_path)


    padded_data = pad(input_data.decode('utf-8'))


    encrypted_data = cipher.encrypt(padded_data.encode('utf-8'))


    write_file(output_file_path, cipher.iv + encrypted_data)


def decrypt_file(input_file_path, output_file_path, key):

    input_data = read_file(input_file_path)


    cipher = AES.new(key, AES.MODE_CBC, iv=input_data[:BLOCK_SIZE])


    decrypted_data = unpad(cipher.decrypt(input_data[BLOCK_SIZE:]))


    write_file(output_file_path, decrypted_data)


key = b'This is a key123'


encrypt_file('data.txt', 'output.txt', key)


decrypt_file('output.txt', 'decrypted.txt', key)
