import sys, os

input_fa = sys.argv[1]
output_dir = sys.argv[2]

#!/usr/bin/env python
f=open(input_fa,"r");
opened = False
for line in f :
    if(line[0] == ">") :
        if(opened) :
            of.close()
        opened = True
        chrname = line[1:].split(" ")[0].rstrip()
        outname = os.path.join(output_dir,chrname+".fa")
        of=open(outname, "w")
        print outname
    of.write(line)
of.close()
