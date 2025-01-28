import hashlib
from typing import Optional, List


class MerkleNode:
    def __init__(self, left: Optional['MerkleNode'], right: Optional['MerkleNode'], hash: str):
        self.left = left  # Left child
        self.right = right  # Right child
        self.hash = hash  # Node hash

    def __repr__(self):
        return f"MerkleNode(hash={self.hash[:8]}, left={self.left is not None}, right={self.right is not None})"


class MerkleTree:
    def __init__(self, data_blocks: List[str]):
        self.leaves = [MerkleNode(None, None, self.hash_data(data)) for data in data_blocks]
        self.root = self.build_tree(self.leaves)

    def hash_data(self, data: str) -> str:
        """Hash the data using SHA-256."""
        return hashlib.sha256(data.encode('utf-8')).hexdigest()

    def build_tree(self, leaves: List[MerkleNode]) -> MerkleNode:
        """Build the Merkle Tree from the leaves."""
        nodes = leaves
        while len(nodes) > 1:
            next_level = []
            for i in range(0, len(nodes), 2):
                left = nodes[i]
                right = nodes[i + 1] if i + 1 < len(nodes) else None
                # Concatenate and hash the left and right child hashes
                combined_hash = self.hash_data(left.hash + (right.hash if right else ""))
                parent_node = MerkleNode(left, right, combined_hash)
                next_level.append(parent_node)
            nodes = next_level  # Move up to the next level
        return nodes[0]  # Root node

    def traverse_tree(self, node: Optional[MerkleNode]):
        """Traverse the tree and print nodes."""
        if node is None:
            return
        print(node)
        self.traverse_tree(node.left)
        self.traverse_tree(node.right)


# Example usage
data_blocks = ["block1", "block2", "block3", "block4"]
merkle_tree = MerkleTree(data_blocks)

print("Root Hash:", merkle_tree.root.hash)
print("\nTree Nodes:")
merkle_tree.traverse_tree(merkle_tree.root)
