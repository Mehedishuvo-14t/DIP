import cv2
import matplotlib.pyplot as plt

image_path = 'mountail.webp'
gray_img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if gray_img is None:
    raise FileNotFoundError(f"Could not open image at {image_path}")

resolutions = [(128, 128), (64, 64), (32, 32), (16, 16)]

plt.figure(figsize=(15, 5))

plt.subplot(1, 5, 1)
plt.imshow(gray_img, cmap='gray')
plt.title(f"Original\n{gray_img.shape[1]}x{gray_img.shape[0]}")
plt.axis("off")

for index, res in enumerate(resolutions, start=2):
    downscaled = cv2.resize(gray_img, res, interpolation=cv2.INTER_AREA)
    upscaled = cv2.resize(downscaled, (gray_img.shape[1], gray_img.shape[0]), interpolation=cv2.INTER_NEAREST)
    
    plt.subplot(1, 5, index)
    plt.imshow(upscaled, cmap='gray')
    plt.title(f"{res[0]}x{res[1]}")
    plt.axis("off")

plt.tight_layout()
plt.show()