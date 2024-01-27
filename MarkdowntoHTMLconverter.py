import markdown
import sys

commandname = sys.argv[1]
inputfile = sys.argv[2]
outputfile = sys.argv[3]
contents = ""
with open(inputfile) as f:
    contents = f.read()
newcontents = markdown.Markdown().convert(contents)

if commandname == "markdown":
    with open(outputfile, 'w') as f:  
        f.write(newcontents)
