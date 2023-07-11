import os
import argparse
import src.hash_calculator
import src.file_verifier

def calculate_hashes(directory, algorithm):
    hashes = {}
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path):
                hashes[file_path] = hash_calculator.calculate_hash(file_path, algorithm)
    return hashes

def main():
    parser = argparse.ArgumentParser(description='File Integrity Checker')
    parser.add_argument('directory', help='directory to calculate hashes')
    parser.add_argument('algorithm', choices=['md5', 'sha256', 'sha512'], help='hash algorithm')
    parser.add_argument('--verify', help='verify file integrity using reference hashes')
    args = parser.parse_args()

    if args.verify:
        reference_hashes = file_verifier.load_reference_hashes(args.verify)
        if reference_hashes:
            results = []
            for file_path in reference_hashes:
                result = file_verifier.verify_file_integrity(file_path, args.algorithm, reference_hashes)
                results.append(result)
            
            for result in results:
                print(f"File: {result['file']} | Hash: {result['hash']} | Status: {result['status']}")
    else:
        hashes = calculate_hashes(args.directory, args.algorithm)
        for file_path, hash_value in hashes.items():
            print(f"File: {file_path} | Hash: {hash_value}")

if __name__ == '__main__':
    main()
