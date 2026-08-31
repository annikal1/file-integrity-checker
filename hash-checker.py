import hashlib

def get_file_hash(filepath):
    """Return the SHA-256 hash (fingerprint) of a file's contents."""
    with open(filepath, "rb") as f:
        content = f.read()
    return hashlib.sha256(content).hexdigest()

if __name__ == "__main__":
    print(get_file_hash("example.txt"))
