import hashlib

def get_file_hash(filepath):
    # return hash of the file
    with open(filepath, "rb") as f:
        content = f.read()
    return hashlib.sha256(content).hexdigest()


def save_hash(filepath, hash_value):
    # save hash file to text file
    with open("fingerprints.txt", "a") as f:
        f.write(f"{filepath}: {hash_value}\n")
        
if __name__ == "__main__":
    print(get_file_hash("example.txt"))
