from simple_blockchain import Blockchain
import json

def main():
    blockchain = Blockchain()

    blockchain.new_transaction("Bob", "Sally", "1 FAKE")
    blockchain.new_transaction("Sally", "Bob", "2 FAKE")
    blockchain.new_block(123)

    blockchain.new_transaction("Bob", "Sam", "3 FAKE")
    blockchain.new_transaction("Sam", "Bill", "0.5 FAKE")
    blockchain.new_transaction("Bill", "Sally", "1 FAKE")
    blockchain.new_block(456789)

    print("Blockchain: ", blockchain.chain) 

    with open('output.json', 'w') as jsonfile:
        json.dump(blockchain.chain, jsonfile)

if __name__ == "__main__":
    main()