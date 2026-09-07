import hashlib
import sys

def get_file_hash(filepath):
    # return hash of the file
    with open(filepath, "rb") as f:
        content = f.read()
    return hashlib.sha256(content).hexdigest()


def save_hash(filepath, hash_value):
    # save hash file to text file
    with open("fingerprints.txt", "a") as f:
        f.write(f"{filepath}: {hash_value}\n")


def get_saved_hash(filepath):
    # Look up the previously saved hash for a given file, if one exists.
    try:
        with open("fingerprints.txt", "r") as f:
            for line in f:
                name, saved_hash = line.strip().split(": ")
                if name == filepath:
                    return saved_hash
    except FileNotFoundError:
        return None
    return None

def check_file(filepath):
    # Compare file's current hash to its saved hash and print the result.
    current_hash = get_file_hash(filepath)
    saved_hash = get_saved_hash(filepath)

    if saved_hash is None:
        print(f"No saved fingerprint found for {filepath}. Saving it now.")
        save_hash(filepath, current_hash)
    elif current_hash == saved_hash:
        print(f"{filepath} is unchanged.")
    else:
        print(f"{filepath} has been modified!")
        
if __name__ == "__main__":
    print(get_file_hash("example.txt"))
