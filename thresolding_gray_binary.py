import cv2
import matplotlib.pyplot as plt

image_path = 'mountail.webp'
gray_img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if gray_img is None:
    raise FileNotFoundError(f"Could not open image at {image_path}")

threshold_val = int(input("Enter threshold value (0-255): "))

test_thresholds = [
    max(0, threshold_val - 50),
    threshold_val,
    min(255, threshold_val + 50)
]

plt.figure(figsize=(15, 5))

plt.subplot(1, 4, 1)
plt.imshow(gray_img, cmap='gray')
plt.title("Original Grayscale")
plt.axis("off")

for i, t in enumerate(test_thresholds, start=2):
    _, binary_img = cv2.threshold(gray_img, t, 255, cv2.THRESH_BINARY)
    plt.subplot(1, 4, i)
    plt.imshow(binary_img, cmap='gray')
    plt.title(f"Threshold = {t}")
    plt.axis("off")

plt.tight_layout()
plt.show()