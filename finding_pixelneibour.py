import cv2

def get_pixel_neighbors(img_shape, coord):
    height, width = img_shape[:2]
    y, x = coord
    
    n4 = []
    nd = []
    n8 = []
    
    if y - 1 >= 0:
        n4.append((y - 1, x))
    if y + 1 < height:
        n4.append((y + 1, x))
    if x - 1 >= 0:
        n4.append((y, x - 1))
    if x + 1 < width:
        n4.append((y, x + 1))
        
    if y - 1 >= 0 and x - 1 >= 0:
        nd.append((y - 1, x - 1))
    if y - 1 >= 0 and x + 1 < width:
        nd.append((y - 1, x + 1))
    if y + 1 < height and x - 1 >= 0:
        nd.append((y + 1, x - 1))
    if y + 1 < height and x + 1 < width:
        nd.append((y + 1, x + 1))
        
    n8 = n4 + nd
    
    return set(n4), set(nd), set(n8)

image_path = 'mountail.webp'
gray_img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if gray_img is None:
    raise FileNotFoundError(f"Could not open image at {image_path}")

h, w = gray_img.shape
test_points = {
    "Middle Pixel": (h // 2, w // 2),
    "Edge Pixel": (0, w // 2),
    "Corner Pixel": (0, 0)
}

for label, point in test_points.items():
    n4, nd, n8 = get_pixel_neighbors(gray_img.shape, point)
    print(f"=== {label} at (y={point[0]}, x={point[1]}) ===")
    print(f"4-Neighbors  N4(p) : {n4}")
    print(f"Diagonal     ND(p) : {nd}")
    print(f"8-Neighbors  N8(p) : {n8}\n")