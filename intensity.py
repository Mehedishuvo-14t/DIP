import cv2
import numpy as np
import matplotlib.pyplot as plt

image_path = 'mountail.webp'
gray_img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if gray_img is None:
    raise FileNotFoundError(f"Could not open image at {image_path}")

gray_levels = [256, 128, 64, 32, 16, 8, 4, 2]

plt.figure(figsize=(16, 8))

for idx, levels in enumerate(gray_levels, start=1):
    factor = 256 // levels
    quantized_img = (gray_img // factor) * factor
    
    plt.subplot(2, 4, idx)
    plt.imshow(quantized_img, cmap='gray', vmin=0, vmax=255)
    plt.title(f"{levels} Gray Levels ({int(np.log2(levels))} bits)")
    plt.axis("off")

plt.tight_layout()
plt.show()