from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from PIL import Image
import os

def encrypt_image(input_image_path, output_image_path, key):
    # Open and read the input image
    input_image = Image.open(input_image_path)
    # Convert the image to RGB mode (if it's not already in RGB)
    input_image = input_image.convert("RGB")
    # Convert the image to bytes
    input_image_bytes = input_image.tobytes()

    # Generate a random initialization vector
    iv = get_random_bytes(16)

    # Create AES cipher object with CBC mode
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Encrypt the image data
    encrypted_image_bytes = cipher.encrypt(pad(input_image_bytes, AES.block_size))

    # Write the encrypted image bytes to the output file
    with open(output_image_path, "wb") as f:
        f.write(iv + encrypted_image_bytes)

def decrypt_image(input_image_path, output_image_path, key):
    # Read the encrypted image data
    with open(input_image_path, "rb") as f:
        encrypted_data = f.read()

    # Extract the initialization vector
    iv = encrypted_data[:16]
    encrypted_image_bytes = encrypted_data[16:]

    # Create AES cipher object with CBC mode
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Decrypt the image data
    decrypted_image_bytes = unpad(cipher.decrypt(encrypted_image_bytes), AES.block_size)

    # Create an image from the decrypted bytes
    decrypted_image = Image.frombytes("RGB", (256, 256), decrypted_image_bytes)

    # Save the decrypted image to the output file
    decrypted_image.save(output_image_path)

def main():
    input_image_path = "input_image.jpg"
    output_encrypted_image_path = "encrypted_image.jpg"
    output_decrypted_image_path = "decrypted_image.jpg"
    
    # Generate a 16-byte (128-bit) encryption key
    key = get_random_bytes(16)

    # Encrypt the input image
    encrypt_image(input_image_path, output_encrypted_image_path, key)
    print("Image encrypted successfully.")

    # Decrypt the encrypted image
    decrypt_image(output_encrypted_image_path, output_decrypted_image_path, key)
    print("Image decrypted successfully.")

if __name__ == "__main__":
    main()
