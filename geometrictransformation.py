import cv2
import numpy as np
import matplotlib.pyplot as plt

image_path = 'mountail.webp'
img = cv2.imread(image_path, cv2.IMREAD_COLOR)

if img is None:
    raise FileNotFoundError(f"Could not open image at {image_path}")

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
h, w = img.shape[:2]

# (a) Translation: Shift 50 pixels right (x), 30 pixels down (y)
M_trans = np.float32([[1, 0, 50], [0, 1, 30]])
translated = cv2.warpAffine(img_rgb, M_trans, (w, h))

# (b) Rotation: Rotate 45 degrees counter-clockwise around center
center = (w // 2, h // 2)
M_rot = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(img_rgb, M_rot, (w, h))

# (c) Scaling: Scale by 0.6x (downscale) inside original dimensions
M_scale = np.float32([[0.6, 0, 0], [0, 0.6, 0]])
scaled = cv2.warpAffine(img_rgb, M_scale, (w, h))

plt.figure(figsize=(12, 8))

titles = ['Original Image', 'Translation (tx=50, ty=30)', 
          'Rotation (45°)', 'Scaling (0.6x)']
transformed_images = [img_rgb, translated, rotated, scaled]

for i in range(4):
    plt.subplot(2, 2, i + 1)
    plt.imshow(transformed_images[i])
    plt.title(titles[i])
    plt.axis('off')

plt.tight_layout()
plt.show()