#Import the required modules
from cryptography.fernet import Fernet

#open the key file
with open("filekey.key", "rb") as filekey:
    key = filekey.read()

#Use the key
fernet = Fernet(key)

#open the encrypted file
with open('Document1.docx', 'rb') as decrypted_file:
    encrypted = decrypted_file.read()

decrypted = fernet.decrypt(decrypted_file):
    decrypted_file.write(decrypted)