import cv2
import numpy as np
import matplotlib.pyplot as plt

image_path = 'mountail.webp'
clean_img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE).astype(np.float32)

if clean_img is None:
    raise FileNotFoundError(f"Could not open image at {image_path}")

# Generate 20 noisy copies with zero-mean Gaussian noise
noisy_images = []
num_copies = 20
sigma = 30 # Noise standard deviation

for _ in range(num_copies):
    noise = np.random.normal(0, sigma, clean_img.shape)
    noisy_img = clean_img + noise
    noisy_images.append(noisy_img)

# Average all noisy copies together
averaged_img = np.mean(noisy_images, axis=0)

# Clip values to valid 8-bit range [0, 255]
single_noisy_display = np.clip(noisy_images[0], 0, 255).astype(np.uint8)
averaged_display = np.clip(averaged_img, 0, 255).astype(np.uint8)
clean_display = clean_img.astype(np.uint8)

plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(clean_display, cmap='gray')
plt.title("Original Clean Image")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(single_noisy_display, cmap='gray')
plt.title("Single Noisy Copy (1 Frame)")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(averaged_display, cmap='gray')
plt.title(f"Averaged Result ({num_copies} Frames)")
plt.axis("off")

plt.tight_layout()
plt.show()