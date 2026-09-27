import cv2
import matplotlib.pyplot as plt

# File path provided
image_path = 'mountail.webp'

# ---------------------------------------------------------
# 1. READ & INSPECT COLOR IMAGE
# ---------------------------------------------------------
# Read image in standard BGR color format
color_img = cv2.imread(image_path, cv2.IMREAD_COLOR)

if color_img is None:
    print(f"Error: Could not load image from '{image_path}'. Please check the file path.")
else:
    # Convert BGR (OpenCV default) to RGB for Matplotlib display
    color_img_rgb = cv2.cvtColor(color_img, cv2.COLOR_BGR2RGB)
    
    # Extract dimensions and properties
    height, width, channels = color_img.shape
    data_type = color_img.dtype

    print("=== COLOR IMAGE PROPERTIES ===")
    print(f"Width               : {width} pixels")
    print(f"Height              : {height} pixels")
    print(f"Color Channels      : {channels}")
    print(f"Data Type           : {data_type}\n")

# ---------------------------------------------------------
# 2. READ & INSPECT GRAYSCALE IMAGE
# ---------------------------------------------------------
# Read image directly in grayscale mode
gray_img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Extract dimensions and properties
# Note: Grayscale images are 2D arrays, so shape only has (height, width)
gray_height, gray_width = gray_img.shape
gray_channels = 1 if len(gray_img.shape) == 2 else gray_img.shape[2]
gray_data_type = gray_img.dtype

print("=== GRAYSCALE IMAGE PROPERTIES ===")
print(f"Width               : {gray_width} pixels")
print(f"Height              : {gray_height} pixels")
print(f"Color Channels      : {gray_channels}")
print(f"Data Type           : {gray_data_type}\n")

# ---------------------------------------------------------
# 3. DISPLAY IMAGES ON SCREEN
# ---------------------------------------------------------
plt.figure(figsize=(10, 5))

# Plot Color Image
plt.subplot(1, 2, 1)
plt.imshow(color_img_rgb)
plt.title("Color Image")
plt.axis("off")

# Plot Grayscale Image
plt.subplot(1, 2, 2)
plt.imshow(gray_img, cmap='gray')
plt.title("Grayscale Image")
plt.axis("off")

plt.tight_layout()
plt.show()