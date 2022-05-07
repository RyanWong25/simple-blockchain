import hashlib          #for encryption
import json             #for block format
from time import time   #for block timestamp

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.pending_transactions = []

        self.new_block(previous_hash = "The Times 03/Jan/2009 Chancellor on brink of second bailout for banks.", proof = 100)