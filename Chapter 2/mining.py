import hashlib

def mining(string , difficulty):
    nonce = 0

    while True:
        data = string + str(nonce)
        hash_value = hashlib.sha256(data.encode()).hexdigest()
        if hash_value[:difficulty] == "0"*difficulty:
            return nonce, hash_value
        nonce += 1


input_string = input("Enter the input string : ")
difficulty = int(input("Enter the difficulty: "))

nonce, hash_val = mining(input_string, difficulty)

print(f"Input String : {input_string}")
print(f"Nonce: {nonce}")
print(f"Generated Hash : {hash_val}")