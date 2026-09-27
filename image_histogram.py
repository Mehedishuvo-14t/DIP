import cv2
import numpy as np
import matplotlib.pyplot as plt

image_path = 'mountail.webp'
base_img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if base_img is None:
    raise FileNotFoundError(f"Could not open image at {image_path}")

dark_img = cv2.convertScaleAbs(base_img, alpha=0.5, beta=0)
bright_img = cv2.convertScaleAbs(base_img, alpha=0.5, beta=128)
low_contrast_img = cv2.convertScaleAbs(base_img, alpha=0.25, beta=100)

test_images = {
    "Dark Image": dark_img,
    "Bright Image": bright_img,
    "Low-Contrast Image": low_contrast_img
}

plt.figure(figsize=(15, 8))

for idx, (title, img) in enumerate(test_images.items(), start=1):
    hist = cv2.calcHist([img], [0], None, [256], [0, 256]).ravel()
    
    plt.subplot(2, 3, idx)
    plt.imshow(img, cmap='gray', vmin=0, vmax=255)
    plt.title(title)
    plt.axis("off")
    
    plt.subplot(2, 3, idx + 3)
    plt.bar(range(256), hist, width=1.0, color='gray')
    plt.xlim([0, 256])
    plt.title(f"Histogram of {title}")

plt.tight_layout()
plt.show()