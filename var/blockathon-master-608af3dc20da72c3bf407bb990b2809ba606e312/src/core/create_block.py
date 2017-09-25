import pickle

def writer(Block, homedirectory):
    block_hash = Block.hash_block()

    print 'Writing block...%s' % (block_hash)
    pickle.dump(Block, open("%s%s" % (homedirectory, block_hash), "wb"))