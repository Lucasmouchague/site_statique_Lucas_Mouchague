#Static site
## Setup:
### Requirement:
You must have python 3 up to date with pip and a github account.
### Download and setup:
Open a console:
```
git clone https://github.com/Lucasmouchague/site_statique_Lucas_Mouchague
cd site_statique_Lucas_Mouchague
```
Once your in the directory you have to install some packages to do that you can execute the command
```
pip install -r requirements.txt
```
### Usage:
Now you are ready to convert your mardown file to an html file for your static site.
You can see all the things you can do with the command:
```
$python3 site-statique.py --help

Usage: site-statique.py [OPTIONS]

Options:
  -i, --input_file TEXT   path of input file without quotes.
  -o, --output_file TEXT  Path of output file without quotes.
  -t, --title TEXT        Title of your website.
  --help                  Show this message and exit.
```
The conversion of the file are make with Mardown2 (https://github.com/trentm/python-markdown2)

#### Example
```
$python3 site-statique.py --input_file path_of_your_input_file/your_file.md --output_file path_of_your_output_file/your_file.html

Conversion successful!
```
You can also add a title to your html page
```
$python3 site-statique.py --input_file path_of_your_input_file/your_file.md --output_file path_of_your_output_file/your_file.html --title your_title

Conversion successful!
```
#### Real usage:
The real usage of this program is to make custom static site on the github platform
To do this create a new repository and name it like this
```
the_name_of_your_repo.github.io
```
![Alt text]()

after that clone it on your computer
```
git clone https://github.com/Lucasmouchague/test.github.io.git
Clonage dans 'test.github.io'...
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Dépaquetage des objets: 100% (3/3), fait.
```
so now you can use the program to generate your html file
```
$python3 site-statique.py --input_file path_of_your_input_file/your_file.md --output_file path_of_your_repository/your_file.html --title your_title

Conversion successful!
```
After commit and push it

```
git add --all

git commit -m "Initial commit"

git push -u origin master
```