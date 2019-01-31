import markdown2
import os

path = input('votre chemin: ')
for files in os.listdir(path):
	input_file = open(files, mode="r", encoding="utf-8")
	text = input_file.read()
	html = markdown2.markdown(text)
	print (html)