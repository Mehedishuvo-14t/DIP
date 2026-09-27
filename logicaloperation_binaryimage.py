import cv2
import numpy as np
import matplotlib.pyplot as plt

# Create canvas
h, w = 300, 300
img1 = np.zeros((h, w), dtype=np.uint8)
img2 = np.zeros((h, w), dtype=np.uint8)

# Draw overlapping white circle and square
cv2.circle(img1, (130, 150), 70, 255, -1)     # White Circle
cv2.rectangle(img2, (120, 80), (230, 220), 255, -1) # White Square

# Compute Set / Logical Operations
bit_and = cv2.bitwise_and(img1, img2)
bit_or  = cv2.bitwise_or(img1, img2)
bit_not = cv2.bitwise_not(img1)
bit_xor = cv2.bitwise_xor(img1, img2)

plt.figure(figsize=(12, 8))

titles = ['Image A (Circle)', 'Image B (Square)', 'AND (Intersection)',
          'OR (Union)', 'NOT (Inverted Circle)', 'XOR (Difference)']
images = [img1, img2, bit_and, bit_or, bit_not, bit_xor]

for i in range(6):
    plt.subplot(2, 3, i + 1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')

plt.tight_layout()
plt.show()