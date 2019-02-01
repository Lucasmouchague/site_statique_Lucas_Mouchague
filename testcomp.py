import markdown2
import time
import os


'''
path = input('votre chemin: ')
for files in os.listdir(path):
	input_file = open(files, mode="r", encoding="utf-8")
	text = input_file.read()
	html = markdown2.markdown(text)
	print (html)
'''
print("[!]refer the path of your files without quotes[!]")
file = input("Path of your file: ")

if file[0] == "'" or file[0] == '"':
	print('bad format of input')
	time.sleep(1)
	exit()
else:
	convert_file = open(file, mode='r', encoding="utf-8")
	text = convert_file.read()
	html = markdown2.markdown(text)
	print(html)
