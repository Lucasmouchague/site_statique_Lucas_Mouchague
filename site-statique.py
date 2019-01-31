import argparse
import markdown2
import os

invalid_input_path = "[!] Error: input path invalid"
invalid_output_path = "[!] Error: output path invalid"

def valid_path(input_path, output_path):
	if not valid_input(path):
		print(invalid_input_path)
		quit()
	if not valid_output(output_path):
		print(invalid_output_path)
		quit()
	return

def valid_input_path(input_path):
	return os.path.exists(input_path)

def valid_output_path(output_path):
	return os.path.exists(output_path)

def convert():
	for files in os.listdir(path):
		print(files)


		#if files.endswith('.md'):



def main():
	parser = argparse.ArgumentParser(description = "Markdown to html program")

	parser.add_argument("-i", "--input_files", type = str, nargs = 1, metavar = "path_files", default = None, help = "Path of files.")

	parser.add_argument("-o", "--output_files", type = str, nargs = 1, metavar = "output_files", default = None, help = "Output path of files")

	args = parser.parse_args()
if __name__ == '__main__':
	main()