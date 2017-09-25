import os

def remove(hash, homedirectory):

    os.remove('%s%s' % (hash, homedirectory))