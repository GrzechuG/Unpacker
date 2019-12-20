import os
import sys
import time
filename= sys.argv[1]
while(True):
    print("File being uncompressed: "+filename)
    out=os.popen("file "+filename).read().split(":")[1]
    print("Next type: "+out)

    if "gzip" in out:
        tmpFilename = filename
        if not filename.endswith(".gz"):
            os.system("mv "+filename+" "+filename+".gz")
            tmpFilename = filename+".gz"
        print("Uncompressing gzip...")
        os.system("gunzip "+tmpFilename)
        print("")
    elif "bzip2" in out:
        tmpFilename = filename
        if not filename.endswith(".bz2"):
            os.system("mv "+filename+" "+filename+".bz2")
            tmpFilename = filename+".bz2"
        print("Uncompressing bzip2...")
        os.system("bzip2 -d "+ tmpFilename)
    elif "POSIX tar" in out:
        if not filename.endswith(".tar"):
            os.system("mv "+filename+" "+filename+".tar")
            filename = filename+".tar"
        print("Uncompressing tar...")
        filename = os.popen("tar -xvf "+filename).read().replace("\n","")
    elif "zip" in out:
        if not filename.endswith(".zip"):
            os.system("mv "+filename+" "+filename+".zip")
            filename = filename+".zip"
        print("Uncompressing zip...")
        os.system("unzip "+filename)
    else:
        print("File has been unpacked successfully! ")
        print("The reulting file output is: "+filename)
        exit()
