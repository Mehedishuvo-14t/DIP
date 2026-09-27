import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load base image
image_path = 'mountail.webp'
img1 = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if img1 is None:
    raise FileNotFoundError(f"Could not open image at {image_path}")

# Create a second image with a small added change (a white rectangle)
img2 = img1.copy()
cv2.rectangle(img2, (100, 100), (200, 200), (255), -1)

# Image Arithmetic
add_img = cv2.add(img1, img2)
sub_img = cv2.subtract(img1, img2) # Absolute difference for change detection
abs_diff = cv2.absdiff(img1, img2)
mul_img = cv2.multiply(img1, img2, scale=1.0/255.0)
div_img = cv2.divide(img1, img2 + 1) # Add 1 to avoid division by zero

plt.figure(figsize=(15, 8))

titles = ['Original', 'Modified (Object Added)', 'Absolute Difference (Change Detection)',
          'Addition', 'Multiplication', 'Division']
images = [img1, img2, abs_diff, add_img, mul_img, div_img]

for i in range(6):
    plt.subplot(2, 3, i + 1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')

plt.tight_layout()
plt.show()