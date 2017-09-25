import read_chain

def validate(hash):
   # print 'Starting validation...'
  #  print 'Validation hash...%s' % hash

    last_block = read_chain.last_block()
    previous_hash = last_block.get_previous_hash()

    hash_list = []
    hash_list.append(last_block.get_hash())

    while (previous_hash != '0'):
        block = read_chain.single_block(previous_hash)
        hash_list.append(block.get_hash())
        previous_hash = block.get_previous_hash()

    if hash in hash_list:
        return True
    else:
        return False
        
        
#    for already_hash in hash_list:
#        print 'Validation hash_list... %s' % (already_hash)