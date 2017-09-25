import datetime as date
import hashlib as hasher

import src.core.create_chain
import src.core.delete_chain
import src.core.read_chain
import src.core.validate_chain
import src.core.write_block
import src.core.poc.remove_block


# Definier hier wat er precies in de block moet.
class Block:

    def __init__(self, index, data, previous_hash):
        self.index = index
        self.data = data
        self.timestamp = date.datetime.now()
        self.previous_hash = previous_hash
        self.hash = self.hash_block()


    def hash_block(self):
        sha = hasher.sha256()
        sha.update(str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash))
        return sha.hexdigest()


    def get_timestamp(self):
        return self.timestamp


    def get_data(self):
        return self.data


    def get_hash(self):
        return self.hash


    def get_index(self):
        return self.index


    def get_previous_hash(self):
        return self.previous_hash

# Generate genesis block
def create_genesis_block():
    # Manually construct a block with
    # index zero and arbitrary previous hash

    genesis_block = Block(0, "Genesis Block", "0")
    src.core.poc.write_block.writer(genesis_block)


def create_block(data):
    last_block = src.core.poc.read_chain.last_block()

    new_block = Block(last_block.get_index() + 1, data, last_block.get_hash())
    src.core.poc.write_block.writer(new_block)

    return new_block.get_hash()


def create_block_safe(data):
    hash = create_block('nieuwe block')

    if src.core.poc.validate_chain.validate(hash) is False:
        src.core.poc.remove_block.remove(hash)


    # Generate all later blocks in the blockchain
def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = "Hey! I'm block " + str(this_index)
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)


# Create the blockchain and add the genesis block
#blockchain = [create_genesis_block()]

src.core.poc.delete_chain.all()
create_genesis_block()
src.core.poc.read_chain.all()

hash = create_block_safe('nieuwe block')

hash = create_block_safe('nieuwe block')

hash = create_block_safe('nieuwe block')

hash = create_block_safe('nieuwe block')

hash = create_block_safe('nieuwe block')

hash = create_block_safe('nieuwe block')

hash = create_block_safe('nieuwe block')

src.core.poc.read_chain.all()

#previous_block = blockchain[0]

# How many blocks should we add to the chain
# after the genesis block
num_of_blocks_to_add = 20

# Add blocks to the chain
#for i in range(0, num_of_blocks_to_add):
#    block_to_add = next_block(previous_block)
#    blockchain.append(block_to_add)
#    previous_block = block_to_add
    # Tell everyone about it!
    #print "Block #{} has been added to the blockchain!".format(block_to_add.index)
    #print "Hash: {}\n".format(block_to_add.hash)

