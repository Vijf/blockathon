import os
import sys

os.chdir(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/../..')

import src.core.attributen_chain
import src.core.image_chain

def main():
    src.core.attributen_chain.create_genesis()
    src.core.image_chain.create_genesis()

main()