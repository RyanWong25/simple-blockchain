import hashlib          #for encryption
import json             #for block format
from time import time   #for block timestamp

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.pending_transactions = []

        self.new_block(previous_hash = "Genesis Block", proof = 100)

    
    def new_block(self, proof, previous_hash = None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.pending_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.pending_transactions = []
        self.chain.append(block)

        return block

    
    @property
    def last_block(self):
        return self.chain[-1]

    
    def new_transaction(self, sender, receiver, amount):
        transaction = {
            'sender': sender,
            'receiver': receiver,
            'amount': amount,
        }
        self.pending_transactions.append(transaction)

        return self.last_block['index'] + 1


    def hash(self, block):
        stringify = json.dumps(block, sort_keys = True)
        block_unicode = stringify.encode()

        raw_hash = hashlib.sha256(block_unicode)
        hex_hash = raw_hash.hexdigest()

        return hex_hash