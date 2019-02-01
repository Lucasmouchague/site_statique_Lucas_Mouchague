import argparse
import markdown2
import os

print("[!]refer the path of your files without quotes[!]")
parser = argparse.ArgumentParser(description = "Markdown to html program")

parser.add_argument("-i", "--input_files", type = str, nargs = 1, metavar = "path_files", default = None, help = "Path of files.")

parser.add_argument("-o", "--output_files", type = str, nargs = 1, metavar = "output_files", default = None, help = "Output path of files")

args = parser.parse_args()

def convert(args.input_files):

	if input_files[0] == "'" or input_files[0] == '"':
		print('bad format of input')
		time.sleep(1)
		exit()
	else:
		convert_file = open(file, mode='r', encoding="utf-8")
		text = convert_file.read()
		html = markdown2.markdown(text)
		print(html)
