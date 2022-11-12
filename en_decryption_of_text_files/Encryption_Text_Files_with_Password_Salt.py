from cryptography.fernet import Fernet
import cryptography
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
import secrets
import base64
import getpass

### Salt and it's generation ###

def generate_salt(size):
    """Generate the salt used for key derivation, 
    `size` is the length of the salt to generate""" 
    return secrets.token_bytes(size)

def derive_key(salt, password):
    """Derive the key from the `password` using the passed `salt`
        @salt: bytes
        @password: text
    """ 
    kdf = Scrypt(salt=salt, length=32, n=2**14, r=8, p=1)
    return kdf.derive(password.encode())

def save_salt(salt, password):
    """Save the salt"""
    salt=derive_key(salt, password)
    with open('salt.salt', "wb") as file: 
        file.write(salt)
        file.close()
def load_salt():
    # load salt from salt.salt file 
    return open("salt.salt", "rb").read()

def generate_key(password, salt_size=16, load_existing_salt=False, save_salt=True): 
    """
    Generates a key from a `password` and the salt.
    If `load_existing_salt` is True, it'll load the salt from a file in the current directory called "salt.salt".
    If `save_salt` is True, then it will generate a new salt
    and save it to "salt.salt"
    """
    if load_existing_salt:
        # load existing salt
        salt = load_salt() 
    elif save_salt:
        # generate new salt and save it
        salt = generate_salt(salt_size)
        with open("salt.salt", "wb") as salt_file:
            salt_file.write(salt)
            salt_file.close()
        # generate the key from the salt and the password 
    derived_key = derive_key(salt, password)
    # encode it using Base 64 and return it
    return base64.urlsafe_b64encode(derived_key)

salt_size=32
salt=generate_salt(size=salt_size)
password='password'

save_salt(salt, password)
generate_key(password, salt_size=salt_size, load_existing_salt=False, save_salt=True)

### Encryption and Decryption ###

def encrypt(filename, key): 
    """Given a filename (str) and key (bytes), 
    it encrypts the file and write it """
    f = Fernet(key)
    with open(filename, "rb") as file: 
        # read all file data 
        file_data = file.read()
        encrypted_data = f.encrypt(file_data)
        
    with open(filename[:-4]+'_enc.key', "wb") as file: 
        file.write(encrypted_data)
        file.close()

def decrypt(filename, key): 
    """Given a filename (str) and key (bytes), 
    it decrypts the file and write it """
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read() # decrypt data
        try:
            decrypted_data = f.decrypt(encrypted_data) # write the original file
        except cryptography.fernet.InvalidToken:
            print("Invalid token, most likely the password is incorrect")
            return
    
    with open(filename[:-8]+'_dec.key', "wb") as file:
        file.write(decrypted_data)
        file.close()

def key_gen():
    key = Fernet.generate_key()
    return key

file_name='keepass_masterkey.key'
with open(file_name, "rb") as file:
        # read the encrypted data
        data = file.read()
        print("Text file:",data)
        file.close()
key=key_gen()
print("Key for En- and Decryption:",key)

encrypt(file_name, key)
with open('keepass_masterkey_enc.key', "rb") as file:
        # read the encrypted data
        data = file.read()
        print("Encrypted text files:",data)
        file.close()

decrypt('keepass_masterkey_enc.key', key)
with open('keepass_masterkey_dec.key', "rb") as file:
        # read the encrypted data
        data = file.read()
        print("Decrypted text file:",data)
        file.close()
