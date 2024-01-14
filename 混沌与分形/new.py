import numpy as np
import cv2

# from PIL import Image
#
# # open colour image
# image_raw = Image.open("1.png")
# # convert image to black and white
# image_black_white = image_raw.convert('1')
# image_black_white.save('111.png')
# image_black_white.show()

def arnold_encrypt(image, iterations):
    height, width = image.shape
    encrypted_image = np.zeros_like(image)

    for i in range(iterations):
        for y in range(height):
            for x in range(width):
                new_y = (2 * y + x) % height
                new_x = (y + x) % width
                encrypted_image[new_y, new_x] = image[y, x]
        image = encrypted_image.copy()

    return encrypted_image


def arnold_decrypt(encrypted_image, iterations):
    height, width = encrypted_image.shape
    decrypted_image = np.zeros_like(encrypted_image)

    for i in range(iterations):
        for y in range(height):
            for x in range(width):
                old_y = (y - x) % height
                old_x = (2 * x - y) % width
                decrypted_image[old_y, old_x] = encrypted_image[y, x]
        encrypted_image = decrypted_image.copy()

    return decrypted_image


# 读取图像
image_path = 'img.png'
image = cv2.imread(image_path, 0)


# 加密图像
iterations = 3
encrypted_image = arnold_encrypt(image, iterations)

# 解密图像
decrypted_image = arnold_decrypt(encrypted_image, iterations)

# 显示图像
cv2.imshow("Original Image", image)
cv2.imshow("Encrypted Image", encrypted_image)
cv2.imwrite("22.png", encrypted_image)
cv2.imshow("Decrypted Image", decrypted_image)
cv2.imwrite("33.png", decrypted_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
