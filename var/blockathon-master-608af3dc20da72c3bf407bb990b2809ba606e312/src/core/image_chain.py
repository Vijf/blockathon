import hashlib as hasher
import datetime as date
import os

import src.core.read_chain
import src.core.validate_chain

import src.core.delete_block
import src.core.create_block

# Attributen chain

homedirectory = '/usr/share/nginx/html/chain/images/'


class Block:

    def __init__(self, image_hash, previous_hash):
        self.image_hash = image_hash
        self.timestamp = date.datetime.now()
        self.previous_hash = previous_hash
        self.hash = self.hash_block()


    def hash_block(self):
        sha = hasher.sha256()
        sha.update(str(self.timestamp) + str(self.image_hash) + str(self.previous_hash))
        return sha.hexdigest()


    def get_timestamp(self):
        return self.timestamp


    def get_image_hash(self):
        return self.image_hash


    def get_hash(self):
        return self.hash


    def get_previous_hash(self):
        return self.previous_hash


### Create chain
def create_genesis():

    sha = hasher.sha256()

    with open('is_it_mr_t.jpg', 'rb') as afile:
        buf = afile.read()
        sha.update(buf)

    image_hash = sha.hexdigest()

    genesis_block = Block(image_hash, "0")
    src.core.create_block.writer(genesis_block, homedirectory)

    os.rename('is_it_mr_t.jpg', "/usr/share/blockathon/upload/%s" % (image_hash))


### Create block
def create_block_instance(image_hash):
    last_block = src.core.read_chain.last_block(homedirectory)

    new_block = Block(image_hash, last_block.get_hash())
    src.core.create_block.writer(new_block, homedirectory)

    return new_block.get_hash()


def create_block_safe(image_hash):
    hash = create_block_instance(image_hash)

    if src.core.validate_chain.validate(hash, homedirectory) is False:
        src.core.delete_block.remove(hash, homedirectory)
        return False
    else:
        return True