import markdown2
import time
import os
import click
import random


@click.command()
@click.option("-i", "--input_file", default = '', help = "path of input file without quotes.")
@click.option("-o", "--output_file", default = '', help = "Path of output file without quotes.")
@click.option("-t", "--title", default = 'site-statique', help = "Title of your website.")


def convert(input_file, output_file, title):
	
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
		output = open(output_file, "w+")
		output.write(HTML_start + html + HTML_end)
		output.close
		print('Conversion successful!')

if __name__ == '__main__':
	convert()