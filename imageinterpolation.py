import cv2
import matplotlib.pyplot as plt

image_path = 'mountail.webp'
gray_img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if gray_img is None:
    raise FileNotFoundError(f"Could not open image at {image_path}")

small_img = cv2.resize(gray_img, (64, 64), interpolation=cv2.INTER_AREA)

target_size = (256, 256)

nearest = cv2.resize(small_img, target_size, interpolation=cv2.INTER_NEAREST)
bilinear = cv2.resize(small_img, target_size, interpolation=cv2.INTER_LINEAR)
bicubic = cv2.resize(small_img, target_size, interpolation=cv2.INTER_CUBIC)

plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(nearest, cmap='gray')
plt.title("Nearest-Neighbor")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(bilinear, cmap='gray')
plt.title("Bilinear")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(bicubic, cmap='gray')
plt.title("Bicubic")
plt.axis("off")

plt.tight_layout()
plt.show()