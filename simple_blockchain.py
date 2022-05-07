import hashlib          #for encryption
import json             #for block format
from time import time   #for block timestamp

class Blockchain(object):
    """
    A class to represent a blockchain.

    ...

    Attributes
    ----------
    chain : list of block
        list of blocks
    pending_transaction : list of transaction
        list of transactions not yet approved and added to new block

    Methods
    -------
    new_block(proof, previous_hash = None):
        Builds a new block with pending transactions and adds it to the chain.
    last_block():
        Gets the most recent block added to the chain.
    new_transactions(sender, receiver, amount):
        Creates a new transaction and adds it to the pending transactions.
    hash(block):
        Creates a new hash given a block using SHA-256 encryption.
    """
    
    def __init__(self):
        """
        Constructs all necessary attributes for the blockchain object.

        Parameters
        ----------
        chain : list of block
            list of blocks
        pending_transaction : list of transaction
            list of transactions not yet approved and added to new block
        """

        self.chain = []
        self.pending_transactions = []

        self.new_block(previous_hash = "Genesis Block", proof = 100)

    
    def new_block(self, proof, previous_hash = None):
        """
        Builds a new block with pending transactions and adds it to the chain.

        Parameters
        ----------
        proof : int
            proof of work value
        previous_hash : str, optional
            hash string of previously approved block

        Returns
        -------
        block : JSON object with block properties
        """
        
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
        """
        Gets the most recent block added to the chain.

        Parameters
        ----------
        None

        Returns
        -------
        chain[-1] (block): The most recently added block
        """

        return self.chain[-1]

    
    def new_transaction(self, sender, receiver, amount):
        """
        Creates a new transaction and adds it to the pending transactions.

        Parameters
        ----------
        sender : str
            string name of transaction sender
        receiver : str
            string name of transaction receiver
        amount : str
            string value of transaction

        Returns
        -------
        last_block['index'] + 1 (int) : index of block this transaction will be added to
        """
        
        transaction = {
            'sender': sender,
            'receiver': receiver,
            'amount': amount,
        }
        self.pending_transactions.append(transaction)

        return self.last_block['index'] + 1


    def hash(self, block):
        """
        Creates a new hash given a block using SHA-256 encryption.

        Parameters
        ----------
        block : JSON object
            JSON object with block properties

        Returns
        -------
        hex_hash (str) : hexidecimal string for new hash from block
        """
        
        stringify = json.dumps(block, sort_keys = True)
        block_unicode = stringify.encode()

        raw_hash = hashlib.sha256(block_unicode)
        hex_hash = raw_hash.hexdigest()

        return hex_hash