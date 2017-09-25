import os
import sys
import hashlib as hasher

os.chdir(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/../..')

import src.core.image_chain
import src.core.attributen_chain

def main(file_name):

    full_path = '/usr/share/nginx/html/upload/%s' % (file_name)

    # Stap 1: Toevoegen afbeelding aan image chain
    image_hash = toevoegen_image(full_path)

    # Stap 2: Toevoegen omschrijving aan attributen chain
    toevoegen_attribute(full_path, image_hash)

def toevoegen_attribute(full_path, image_hash):

    fIn = open('%s.txt' % full_path, "r")
    data = fIn.read()
    fIn.close()

    if src.core.attributen_chain.create_block_safe(data, image_hash) is True:
        os.remove('%s.txt' % full_path)
    else:
        pass


def toevoegen_image(full_path):
    sha = hasher.sha256()

    with open('%s.jpg' % full_path, 'rb') as afile:
        buf = afile.read()
        sha.update(buf)

    image_hash = sha.hexdigest()

    if src.core.image_chain.create_block_safe(image_hash) is True:
        os.rename('%s.jpg' % full_path, "/usr/share/blockathon/upload/%s.jpg" % (image_hash))
    else:
        pass

    return image_hash
