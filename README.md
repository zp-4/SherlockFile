# SherlockFile: File integrity checker


The File Integrity Checker is a Python script that calculates cryptographic hashes of files in a given directory and allows users to verify file integrity by comparing hash values with known reference values.

## Features

- Calculate cryptographic hashes (MD5, SHA256, SHA512) of files in a directory.
- Verify file integrity by comparing hash values with reference hashes.
- Support for multiple hashing algorithms.
- Detailed output displaying the filename, hash value, and verification status.

## Requirements

- Python 3.x

## Usage

1. Clone the repository or download the `file_integrity_checker.py`, `hash_calculator.py`, and `file_verifier.py` files.

2. Open a terminal or command prompt and navigate to the directory containing the script files.

3. Run the following command to execute the File Integrity Checker:

> python file_integrity_checker.py <directory> <algorithm> [--verify <reference_file>]


Replace `<directory>` with the path to the directory you want to calculate hashes for.
Replace `<algorithm>` with the desired hash algorithm: `md5`, `sha256`, or `sha512`.
Optionally, provide `--verify <reference_file>` to verify file integrity using reference hashes. Replace `<reference_file>` with the path to the file containing the reference hashes.

4. Review the output:

- If calculating hashes without verification, the script will display the filename and corresponding hash value for each file in the specified directory.
- If verifying file integrity, the script will display the filename, hash value, and verification status (Verified, Not Verified, or Hash not found) for each file.


## Examples

- Calculate MD5 hashes for files in the `documents` directory:

> python file_integrity_checker.py documents md5

- Calculate SHA256 hashes for files in the `photos` directory and verify file integrity using the `reference_hashes.json` file:

> python file_integrity_checker.py photos sha256 --verify reference_hashes.json


## Example Reference Hashes

Here's an example of how the `reference_hashes.json` file can be structured:

```json
{
"documents/file1.txt": "5eb63bbbe01eeed093cb22bb8f5acdc3",
"documents/file2.txt": "098f6bcd4621d373cade4e832627b4f6",
"photos/image1.jpg": "b7e1be14cd4053ac67b29563b3c5d49c",
"photos/image2.jpg": "c4ca4238a0b923820dcc509a6f75849b"
}
```

In this example, the reference_hashes.json file contains a JSON object where each key represents the file path relative to the directory being checked, and the corresponding value is the expected hash value for that file.

Make sure to update the file path and hash values according to your specific use case.

License
This project is licensed under the [unlicense](LICENSE).
