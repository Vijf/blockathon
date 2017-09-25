import os
import pickle
import glob


def all(homedirectory):

    for filename in os.listdir(homedirectory):

        Block = pickle.load(open('%s/%s' % (homedirectory, filename), "rb"))
        print "%%s:%s:%s:%s" % (Block.get_previous_hash(), Block.get_hash(), Block.get_timestamp(), Block.get_data())


def last_block(homedirectory):
    list_of_files = glob.glob('%s/*' % (homedirectory))  # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getctime)

    Block = pickle.load(open(latest_file, "rb"))

    #print 'Reading last block...%s' % Block.get_hash()

    return Block

def single_block(hash, homedirectory):
    Block = pickle.load(open('%s/%s' % (homedirectory, hash), "rb"))

    return Block