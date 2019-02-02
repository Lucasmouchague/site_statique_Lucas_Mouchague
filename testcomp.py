import markdown2
import time
import os
import click

'''
path = input('votre chemin: ')
for files in os.listdir(path):
	input_file = open(files, mode="r", encoding="utf-8")
	text = input_file.read()
	html = markdown2.markdown(text)
	print (html)
'''

@click.command()
@click.option("--input_file", default = '', help = "path of input file")
@click.option("--output_file", default = '', help = "Path of output file")


def convert_test(input_file, output_file):
	file = input_file
	if file[0] == "'" or file[0] == '"':
		print('bad format of input')
		time.sleep(1)
		exit()
	else:
		convert_file = open(file, mode='r', encoding="utf-8")
		text = convert_file.read()
		html = markdown2.markdown(text)
		f = open(output_file)
		f.write(html)
		f.close

if __name__ == '__main__':
	convert_test()