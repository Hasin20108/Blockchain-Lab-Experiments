import hashlib

indent = " "
first = " "
add = " " * 5

def print_tree(hashes):
    global first, indent, add
    print(first, end= "")
    [print(s[:8] + indent, end= " ") for s in hashes]
    first += add
    print('\n')
    indent += " "

def build_merkle_tree(leaves, depth = 0):
    num_leaves = len(leaves)

    if num_leaves == 1:
        print_tree(leaves)
        return leaves[0]
    
    if num_leaves %2 == 1:
        leaves.append(leaves[-1])
        num_leaves += 1
    
    pairs = [leaves[i] + leaves[i+1] for i in range(0,num_leaves,2)]

    hashes = [hashlib.sha256(pair.encode()).hexdigest() for pair in pairs]
    

    print_tree(leaves)

    return build_merkle_tree(hashes,  depth+1)


rawleaves = ["Hasin", "Sanjoy", "Niloy", "Miju", "Shimla"]
leaves =[hashlib.sha256(leave.encode()).hexdigest() for leave in rawleaves]
# print_tree(leaves)
merkle_root = build_merkle_tree(leaves)

# print("Merkle Root = ", merkle_root)



# print_merkle_tree(merkle_root)