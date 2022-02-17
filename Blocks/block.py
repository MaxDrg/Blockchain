import json
import os
import hashlib

blockchain_dir = os.getcwd() + "\\Blocks\\Blocks\\"

def hashing(filename):
    file = open(blockchain_dir + filename, 'rb').read()
    return hashlib.md5(file).hexdigest()

def get_files():
    print (blockchain_dir)
    files = os.listdir(blockchain_dir)
    return sorted(files)

def check_integrity():
    files = get_files()

    result = []

    for file in files[1:]:
        with open(blockchain_dir + str(file)) as file_block:
            hash = json.load(file_block)['hash']

            prev_file = str(int(file) - 1)
            current_hash = hashing(prev_file)

            if hash == current_hash:
                answer = 'OK'
            else:
                answer = 'Error'

            print('block {} is {}'.format(prev_file, answer)) 

            result.append({'block': prev_file, 'result': answer})
    return result

def create_block(name, amount, to, prev_hash=''):
    files = get_files()
    prev_file = files[-1]
    print(prev_file)

    filename = str(int(prev_file) + 1)

    prev_hash = hashing(str(prev_file))

    data = { 'name': name,
    'amount': amount,
    'to': to,
    'hash': prev_hash
    }

    with open(blockchain_dir + filename, 'w') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)