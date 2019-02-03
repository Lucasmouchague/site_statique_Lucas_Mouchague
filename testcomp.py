import markdown2
import time
import os
import click
import random

'''
path = input('votre chemin: ')
for files in os.listdir(path):
	input_file = open(files, mode="r", encoding="utf-8")
	text = input_file.read()
	html = markdown2.markdown(text)
	print (html)
'''

@click.command()
@click.option("-i", "--input_file", default = '', help = "path of input file")
@click.option("-o", "--output_file", default = '', help = "Path of output file")
@click.option("-t", "--title", default = 'site-statique', help = "Title of your website")
@click.option("-k", "--kikoo_lol", default = False, help = "If True add some kikoo word")

def convert(input_file, output_file, title, kikoo_lol):
	
	HTML_start = '<!DOCTYPE html>\n<html>\n<head>\n<title>' + title + '</title>\n</head>\n<body>\n' 
	HTML_end = '</body>\n</html>'
	file = input_file
	
	if output_file == '':
		print('No output exiting...')
		time.sleep(1)
		quit()

	if file[0] == "'" or file[0] == '"':
		print('bad format of input')
		time.sleep(1)
		exit()
	else:
		convert_file = open(file, mode='r', encoding="utf-8")
		text = convert_file.read()
		html = markdown2.markdown(text)
		'''
		if kikoo_lol == True:
			kikoo_list = ["<p>Kikoo</p>", "<p>lol</p>", "<p>mdr</p>", "<p>ptdr</p>"]
			html.append(random.choice(kikoo_list))
		'''
		output = open(output_file, "w+")
		output.write(HTML_start + html + HTML_end)
		output.close
		print('Conversion successful!')

if __name__ == '__main__':
	convert()