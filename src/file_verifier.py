import os
import json

def load_reference_hashes(reference_file):
    if os.path.isfile(reference_file):
        with open(reference_file) as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                print("Error: Invalid reference file format.")
    else:
        print(f"Error: Reference file '{reference_file}' not found.")
    return {}

def verify_file_integrity(file_path, algorithm, reference_hashes):
    if file_path in reference_hashes:
        expected_hash = reference_hashes[file_path]
        calculated_hash = calculate_hash(file_path, algorithm)
        
        if calculated_hash == expected_hash:
            status = "Verified"
        else:
            status = "Not Verified"
    else:
        status = "Hash not found"
    
    return {
        'file': file_path,
        'hash': calculated_hash,
        'status': status
    }
