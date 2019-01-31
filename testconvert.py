import markdown2
input_file = open("/home/nawak/git/site_statique/", mode="r", encoding="utf-8")
text = input_file.read()
html = markdown2.markdown(text)
print (html)
