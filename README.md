🧱 Basic Blockchain Implementation in Python
📌 Project Description

This project is a simple blockchain implementation in Python that demonstrates the core principles of blockchain technology such as blocks, hashing, proof-of-work, and chain validation.
It is intended for learning purposes and provides a foundation for understanding how decentralized ledgers like Bitcoin or Ethereum work at the most basic level.

⚙️ Features

Block Structure: Each block contains an index, timestamp, transaction/data, nonce, and hash.

Genesis Block: The first block in the blockchain is manually created.

Proof of Work (Mining): A simple mining algorithm ensures that each block’s hash starts with a certain number of zeros (difficulty).

Chain Validation: Ensures data integrity by checking hashes and previous hash links.

Transaction Support: Each block can store custom transaction data (e.g., {"amount": 50}).

Easy to Extend: Can be upgraded to support networking, wallets, or smart contracts.

🔑 How It Works

Genesis Block → The blockchain starts with a special first block.

Adding New Blocks → When a new block is created, it references the previous block’s hash.

Hashing → Each block’s content is hashed using SHA-256 to ensure immutability.

Proof of Work → Mining involves incrementing a nonce until the block’s hash starts with a given number of zeros (difficulty).

Validation → The blockchain is valid only if:

Each block’s hash is correct.

Each block points correctly to the previous block’s hash.
