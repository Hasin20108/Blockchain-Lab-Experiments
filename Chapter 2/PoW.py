import hashlib
import time

class Block:
    def __init__(self, height, data, prev_hash, difficulty):
        self.height = height
        self.data = data
        self.prev_hash = prev_hash
        self.timestamp = time.time()
        self.nonce = 0
        self.difficulty = difficulty
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        res = ''
        while res.startswith('0' * self.difficulty) is False:
            res = hashlib.sha256((str(self.height)+str(self.data) + str(self.prev_hash) + str(self.timestamp) + str(self.nonce)).encode()).digest().hex()
            self.nonce += 1
        self.nonce -=1
        return res
    def regenerate_hash(self):
        res = hashlib.sha256((str(self.height)+str(self.data) + str(self.prev_hash) + str(self.timestamp) + str(self.nonce)).encode()).digest().hex()

        return res        

class Blockchain:
    def __init__(self):
        self.chain = []
        self.createGenesisBlock()
    
    def createGenesisBlock(self):
        x = Block(0, 'Genesis Block', '0'* 64, 4)
        print(f"Genesis Block is Successfully Mined")
        self.chain.append(x)
    
    def addBlock(self, data, difficulty):
        last_block = self.chain[-1]
        prev_hash = last_block.hash
        block_height = last_block.height + 1
        newBlock = Block(block_height, data, prev_hash, difficulty)
        print(f"Block {block_height} is successfully mined by nonce = {newBlock.nonce} with difficulty level {difficulty}")
        self.chain.append(newBlock)
    
    def is_chain_valid(self):
        for i in range(1,  len(self.chain)):
            current_block = self.chain[i]
            prev_block = self.chain[i-1]

            if current_block.hash != current_block.regenerate_hash():
                return False
            if current_block.prev_hash != prev_block.hash:
                return False
    
        return True

if __name__ == '__main__':
    x = Blockchain()

    x.addBlock("Transaction 1", 4)
    x.addBlock("Transaction 2", 4)
    x.addBlock("Transaction 3", 4)

    if x.is_chain_valid():
        print("Chain is Protected")
    else:
        print("Alert! Chain is Corrupted")

   