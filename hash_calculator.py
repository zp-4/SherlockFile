import hashlib

def calculate_hash(file_path, algorithm):
    with open(file_path, 'rb') as file:
        hash_object = hashlib.new(algorithm)
        while chunk := file.read(4096):
            hash_object.update(chunk)
    return hash_object.hexdigest()
