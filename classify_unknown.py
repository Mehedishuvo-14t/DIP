import cv2
import numpy as np
import os

def classify_image(image_path):
    # 1. Check if file exists
    if not os.path.exists(image_path):
        print(f"Error: File '{image_path}' not found.")
        return

    # 2. Read the image as-is (cv2.IMREAD_UNCHANGED preserves original channels)
    img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

    if img is None:
        print(f"Error: Unable to read image file '{image_path}'.")
        return

    # 3. Analyze dimensions and channels
    shape = img.shape
    
    # Check if image has multiple channels (3 for BGR/RGB, 4 for BGRA/RGBA)
    if len(shape) == 3 and shape[2] > 1:
        num_channels = shape[2]
        
        # Check if all color channels are identical (e.g., a grayscale image saved as 3-channel RGB)
        channel_diff_1 = np.array_equal(img[:, :, 0], img[:, :, 1])
        channel_diff_2 = np.array_equal(img[:, :, 1], img[:, :, 2])
        
        if channel_diff_1 and channel_diff_2:
            # Multi-channel array, but all channels carry identical pixel values
            unique_values = np.unique(img[:, :, 0])
            num_unique = len(unique_values)
            
            if num_unique <= 2:
                print(f"Classification : BINARY IMAGE")
                print(f"Reasoning      : Image has {num_channels} identical channels with only {num_unique} unique pixel value(s) {list(unique_values)}.")
            else:
                print(f"Classification : GRAYSCALE IMAGE")
                print(f"Reasoning      : Image has {num_channels} channels, but all channel values are identical across pixels (single intensity representation with {num_unique} unique gray levels).")
        else:
            print(f"Classification : FULL-COLOR IMAGE")
            print(f"Reasoning      : Image contains {num_channels} distinct color channels with differing color values per pixel.")

    # Single-channel array (2D array)
    else:
        unique_values = np.unique(img)
        num_unique = len(unique_values)

        if num_unique <= 2:
            print(f"Classification : BINARY IMAGE")
            print(f"Reasoning      : Single-channel image containing only {num_unique} unique pixel value(s) {list(unique_values)}.")
        else:
            print(f"Classification : GRAYSCALE IMAGE")
            print(f"Reasoning      : Single-channel image with {num_unique} unique intensity values (ranging from {img.min()} to {img.max()}).")

# --- Example Usage ---
image_path = 'mountail.webp'
print(f"Analyzing file: '{image_path}'")
print("-" * 50)
classify_image(image_path)