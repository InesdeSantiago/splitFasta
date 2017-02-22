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
        outname = os.path.join(output_dir,line[1:].rstrip())
        of=open("%s.fa" % (outname, "w")
        print(line[1:].rstrip())
    of.write(line)
of.close()
