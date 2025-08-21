import hashlib
import time

# Class representing a single Block


class Block:
    def __init__(self, index, previous_hash, timestamp, data, nonce=0):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = (str(self.index) +
                        str(self.previous_hash) +
                        str(self.timestamp) +
                        str(self.data) +
                        str(self.nonce))
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self, difficulty):
        # Proof of Work: hash must start with difficulty number of "0"s
        while self.hash[:difficulty] != "0" * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()
        print(f"Block mined: {self.hash}")


# Class representing the Blockchain
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4  # Increase for harder mining

    def create_genesis_block(self):
        return Block(0, "0", time.time(), "Genesis Block")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            # Recalculate hash and compare
            if current.hash != current.calculate_hash():
                print("Current hash not equal")
                return False

            if current.previous_hash != previous.hash:
                print("Previous hash not equal")
                return False

        return True


# Testing the Blockchain
if __name__ == "__main__":
    my_blockchain = Blockchain()
    print("Mining block 1...")
    my_blockchain.add_block(Block(1, "", time.time(), {"amount": 50}))

    print("Mining block 2...")
    my_blockchain.add_block(Block(2, "", time.time(), {"amount": 100}))

    print("\nBlockchain valid?", my_blockchain.is_chain_valid())

    # Print the blockchain
    for block in my_blockchain.chain:
        print(vars(block))
