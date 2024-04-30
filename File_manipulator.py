import sys
commandname = sys.argv[1]
inputpath = sys.argv[2]
outputpath = sys.argv[3]
contents = ""
with open(inputpath) as f:
    contents = f.read()
newcontents = ""

if commandname == "reverse":
    for i in range(len(contents)):
        newcontents = newcontents + contents[len(contents)-1-i]
    with open(outputpath, 'w') as f:    
        f.write(newcontents)

elif commandname == "copy":
    newcontents = contents
    with open(outputpath, 'w') as f:    
        f.write(newcontents)

elif commandname == "duplicate-contents":
    newcontents = contents*int(outputpath)
    with open(inputpath, 'w') as f:    
        f.write(newcontents)


elif commandname == "replace-string":
    newcontents = contents.replace(outputpath,sys.argv[4])
    with open(inputpath, 'w') as f:    
        f.write(newcontents)
