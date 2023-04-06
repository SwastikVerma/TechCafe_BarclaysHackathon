import boto3
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.padding import PKCS7


# Set up AWS KMS client
kms = boto3.client('kms', region_name='ap-south-1')


def encrypt_file_with_aes_cbc(input_file_path, output_file_path, key_arn):
    # Generate a data key from KMS
    response = kms.generate_data_key(KeyId=key_arn, KeySpec='AES_256')
    plaintext_key = response['Plaintext']
    ciphertext_key = response['CiphertextBlob']

    # Read the input file and encrypt it using the AES-CBC algorithm
    with open(input_file_path, 'rb') as input_file:
        input_data = input_file.read()
        iv = os.urandom(16)  # Generate a random initialization vector
        cipher = Cipher(algorithms.AES(plaintext_key), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        padder = PKCS7(algorithms.AES.block_size).padder()
        padded_data = padder.update(input_data) + padder.finalize()
        ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    # Write the encrypted file to disk
    with open(output_file_path, 'wb') as output_file:
        output_file.write(iv)
        output_file.write(ciphertext)

    # Upload the encrypted file to S3
    s3 = boto3.client('s3', region_name='ap-south-1')
    s3.upload_file(output_file_path, 'finalbucketbarclays', output_file_path)

    # Delete the plaintext key from memory
    del plaintext_key
#random comment for commit
# Example usage
encrypt_file_with_aes_cbc("C:\\Users\\twadd\\Downloads\\test.csv", "C:\\Users\\twadd\\Downloads\\enctest1.csv", "arn:aws:kms:ap-south-1:241639010922:key/e2f39822-2499-4cd3-a94f-4d20cdd6a956")