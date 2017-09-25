from os import listdir
from os.path import isfile, join

import image_create_new_block
import time

def main():
    mypath = '/usr/share/nginx/html/upload/'

    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

    print onlyfiles

    for filename in onlyfiles:
        if ".jpg" in filename:
            print filename
            file_name = filename.split(".")[0]
            image_create_new_block.main(file_name)
            time.sleep(5)
main()
