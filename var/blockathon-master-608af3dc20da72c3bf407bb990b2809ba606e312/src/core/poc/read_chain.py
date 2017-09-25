import os
import pickle
import glob

working_dir = '/usr/local/blockathon'

def all():

    for filename in os.listdir(working_dir):

        Block = pickle.load(open('%s/%s' % (working_dir, filename), "rb"))
        print "%s:%s:%s:%s:%s" % (Block.get_index(), Block.get_previous_hash(), Block.get_hash(), Block.get_timestamp(), Block.get_data())


def last_block():
    list_of_files = glob.glob('%s/*' % (working_dir))  # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getctime)

    Block = pickle.load(open(latest_file, "rb"))

    #print 'Reading last block...%s' % Block.get_hash()

    return Block

def single_block(hash):
    Block = pickle.load(open('%s/%s' % (working_dir, hash), "rb"))

    return Block