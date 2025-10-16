#Import the required modules
from cryptography.fernet import Fernet

#open the key file
with open("filekey.key", "rb") as filekey:
    key = filekey.read()

#Use the key
fernet = Fernet(key)

#Open file to be encrypted
with open('Document1.docx', 'rb') as file:
    unencrypted = file.key()

#Encrypt the data
encrypted = fernet.encrypt(unencrypted)


#Write the encrypted data
with open('Document1.docx', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)
