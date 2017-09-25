import os
import pickle

def writer(Block):
    block_hash = Block.hash_block()

    print 'Writing block...%s' % (block_hash)
    pickle.dump(Block, open("/usr/local/blockathon/%s" % (block_hash), "wb"))

    #print 'Writing done...'