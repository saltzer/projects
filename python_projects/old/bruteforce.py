from zipfile import ZipFile
from os import mkdir

line = "----------------------------------"
def generator(string):
	for word in string:
		password = word.replace('\n','')
		archive.setpassword(password.encode())
		try:
			archive.extractall(directory)
		except:
			yield "[FALSE]: " + password
		else:
			yield line + "\n[TRUE]: " + password; return

directory = "HackArchive"
try: mkdir(directory)
except FileExistsError: pass

print(line)
with open(input("Dictionary: "), errors='ignore') as dictionary:
	with ZipFile(input("Archive: ")) as archive:
		print(line)
		for password in generator(dictionary):
			print(password)
print(line)
