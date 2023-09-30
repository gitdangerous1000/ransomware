import os
from cryptography.fernet import Fernet
print("...bibliotecas importadas")


# Collect files

def get_file_list():
	files = []
	for file in os.listdir():
		if file == "encrypt.py" or file == "decrypt.py" or file == "key_file.key":
			continue
		if os.path.isfile(file):
			files.append(file)

	print("Os arquivos encontrados são:", files)
	return files


# GET Key

def get_key():
	with open("key_file.key", "rb") as f:
		key = f.read()
	print("...chave encontrada")
	return key


# Decrypt

def decryption_process(files, key):
    password = input("Digite a senha para descriptografar:")
    if password == "senha":
        print("Descriptografia iniciada...")
        for file in files:
            with open(file, "rb") as f:
                content = f.read()
            decrypted_content = Fernet(key).decrypt(content)
            with open(file, "wb") as f:
                f.write(decrypted_content)
                
        print("...descriptografia completa")


# function calls

files = get_file_list()
key = get_key()
decryption_process(files, key)