# create a folder named "data" inside current folder of vs code terminal

import requests
import json
import os
class BaseDB:
    def __init__(self):
        self.basepath = 'data'
        self.filepath = '/'.join((self.basepath, self.filename))
    
    def read(self):
        if not os.path.exists(self.filepath):
            print(f"File {self.filepath} is not available")
            return False

        data = []  # Initialize an empty list to store the JSON objects

        with open(self.filepath, 'r') as file:
            for line in file:  # Read the file line by line
                line = line.strip()  # Remove any leading/trailing whitespace

                if not line:
                    continue  # Check if the line is not empty
                try:
                    data.append(json.loads(line))  # Parse the JSON and add to the list
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON: {e} - Line: {line}")

        return data
    
    def write(self,data):
        json_data = json.dumps(data)
        with open(self.filepath, 'a') as file:
            file.write(json_data + '\n')


class CreateDB(BaseDB):
    def __init__(self):
        self.filename = 'transaction'
        super().__init__() 

    
def get_latest_block(api_key):
    url = "https://api.etherscan.io/api"
    params = {
        "module": "proxy",
        "action": "eth_getBlockByNumber",
        "tag": "latest",
        "boolean": "true",  # This should be "true" (String) for getting full transaction objects.
        "apikey": api_key,
    }

    try:
        # Sending request to the API
        response = requests.get(url, params=params)
        
        # Check if the response was successful
        if response.status_code == 200:
            data = response.json()

            # Print the raw data to verify its structure
            print("API Response Data:", data)

            # Check if the API response has 'result' data
            if data.get('result'):
                return data['result']
            else:
                print(f"Error: {data.get('message', 'No result data available')}")
                return None
        else:
            print(f"Request failed with status code: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"Request failed: {str(e)}")
        return None


def print_block_info(block):
    database = CreateDB()
    if block:
        try:
            print("Latest block information:")
            print(f"Block Number: {int(block['number'], 16)}")
            print(f"Timestamp: {int(block['timestamp'], 16)}")
            print(f"Miner Address: {block['miner']}")
            print(f"Difficulty: {int(block['difficulty'], 16)}")
            print(f"Total Difficulty: {int(block['totalDifficulty'], 16)}")
            print(f"Gas Limit: {int(block['gasLimit'], 16)}")
            print(f"Gas Used: {int(block['gasUsed'], 16)}")
            print(f"Transaction Count: {len(block['transactions'])}")
            print("Transactions:")

            for tx in block['transactions']:
                a = f"Transaction Hash: {tx['hash']}"
                b = f", From: {tx['from']}"
                c = f", To: {tx['to']}"
                d = f", Value (in Wei): {tx['value']}"
                # e = "\n"
                database.write((a + b+ c+ d ))
        except KeyError as e:
            print(f"Error accessing block data: {e}")
    else:
        print("No block information to display.")


# Replace "YOUR_API_KEY" with your actual Etherscan API key
api_key = "7SYMK8T9QYE7FTZ2MK6R3TXX3GWXBWFM9G"

# Fetch the latest block
latest_block = get_latest_block(api_key)

# Print the block information
print_block_info(latest_block)


