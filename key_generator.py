"""Generates an encryption key"""

#Import the required modules
from cryptography.fernet import Fernet

#Generate a key
key = Fernet.generate_key()

#write the key to a file
with open('filekey.key', 'wb') as filekey:
    filekey.write(key)
