import cv2
import matplotlib.pyplot as plt
import os

# File path
image_path = 'mountail.webp'

# ---------------------------------------------------------
# 1. READ COLOR IMAGE & CONVERT TO GRAYSCALE
# ---------------------------------------------------------
# Read original BGR image
color_img = cv2.imread(image_path, cv2.IMREAD_COLOR)

if color_img is None:
    print(f"Error: Could not load image from '{image_path}'.")
else:
    # Convert BGR to RGB (for correct display in Matplotlib)
    color_img_rgb = cv2.cvtColor(color_img, cv2.COLOR_BGR2RGB)

    # Convert RGB to Grayscale using OpenCV built-in function
    gray_img = cv2.cvtColor(color_img, cv2.COLOR_BGR2GRAY)

    # ---------------------------------------------------------
    # 2. REPORT PROPERTIES & DATA SIZE (IN BYTES)
    # ---------------------------------------------------------
    # Number of channels
    color_channels = color_img.shape[2]
    gray_channels = 1  # 2D array representation

    # Data size in memory (in bytes)
    color_size_bytes = color_img.nbytes
    gray_size_bytes = gray_img.nbytes

    print("=== BEFORE CONVERSION (COLOR) ===")
    print(f"Dimensions          : {color_img.shape[1]}x{color_img.shape[0]}")
    print(f"Number of Channels  : {color_channels}")
    print(f"Data Type           : {color_img.dtype}")
    print(f"Memory Size         : {color_size_bytes:,} bytes ({color_size_bytes / 1024:.2f} KB)\n")

    print("=== AFTER CONVERSION (GRAYSCALE) ===")
    print(f"Dimensions          : {gray_img.shape[1]}x{gray_img.shape[0]}")
    print(f"Number of Channels  : {gray_channels}")
    print(f"Data Type           : {gray_img.dtype}")
    print(f"Memory Size         : {gray_size_bytes:,} bytes ({gray_size_bytes / 1024:.2f} KB)\n")

    print(f"Data Size Reduction : {((color_size_bytes - gray_size_bytes) / color_size_bytes) * 100:.2f}% reduction")

    # ---------------------------------------------------------
    # 3. DISPLAY SIDE BY SIDE
    # ---------------------------------------------------------
    plt.figure(figsize=(12, 6))

    # Plot Original Color Image
    plt.subplot(1, 2, 1)
    plt.imshow(color_img_rgb)
    plt.title("Original Color Image (3 Channels)")
    plt.axis("off")

    # Plot Grayscale Image
    plt.subplot(1, 2, 2)
    plt.imshow(gray_img, cmap='gray')
    plt.title("Grayscale Image (1 Channel)")
    plt.axis("off")

    plt.tight_layout()
    plt.show()