import numpy as np
import cv2


def logistic_map(x, r, num_iterations):
    """Logistic Map equation"""
    X = []
    for i in range(num_iterations):
        x1 = r * x * (1 - x)
        x = x1
        X.append(x)
    return X



def encrypt_image(r):
    """Encrypts an image using logistic map and XOR algorithm"""
    # Generate chaos key
    height, width = image.shape
    key = np.zeros((height, width), dtype=np.float64)
    chaotic_sequence = logistic_map(0.5, r, height * width)
    chaotic_sequence = np.reshape(chaotic_sequence, (height, width))
    key = chaotic_sequence.copy()

    # Perform XOR encryption
    encrypted_image = cv2.bitwise_xor(image, np.uint8(key * 255))
    return encrypted_image


def decrypt_image(encrypted_image, r):
    """Decrypts an encrypted image using logistic map and XOR algorithm"""
    height, width = encrypted_image.shape

    # Generate chaos key
    key = np.zeros((height, width), dtype=np.float64)
    chaotic_sequence = logistic_map(0.5, r, height * width)
    chaotic_sequence = np.reshape(chaotic_sequence, (height, width))
    key = chaotic_sequence.copy()

    # Perform XOR decryption
    decrypted_image = cv2.bitwise_xor(encrypted_image, np.uint8(key * 255))
    return decrypted_image


# Example usage
image_path = 'img.png'
image = cv2.imread(image_path,0)
r = 3.9
num_iterations = 100
encrypted_image = encrypt_image(r)
decrypted_image = decrypt_image(encrypted_image, r)

# Display the original, encrypted, and decrypted images
cv2.imshow('Original Image', image)
cv2.imshow('Encrypted Image', encrypted_image)
cv2.imwrite("2_22.png", encrypted_image)
cv2.imshow('Decrypted Image', decrypted_image)
cv2.imwrite("2_33.png", decrypted_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
