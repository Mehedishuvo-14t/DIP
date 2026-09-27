import numpy as np

def compute_distances(p1, p2):
    y1, x1 = p1
    y2, x2 = p2
    
    # Euclidean Distance: sqrt((x1 - x2)^2 + (y1 - y2)^2)
    d_euclidean = np.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    
    # City-Block Distance (D4): |x1 - x2| + |y1 - y2|
    d_cityblock = abs(x1 - x2) + abs(y1 - y2)
    
    # Chessboard Distance (D8): max(|x1 - x2|, |y1 - y2|)
    d_chessboard = max(abs(x1 - x2), abs(y1 - y2))
    
    return d_euclidean, d_cityblock, d_chessboard

# Test Cases
test_cases = [
    ("Test Case 1 (Middle to Middle)", (10, 20), (14, 23)),
    ("Test Case 2 (Diagonal Shift)", (5, 5), (1, 2))
]

for name, p1, p2 in test_cases:
    d_euc, d_4, d_8 = compute_distances(p1, p2)
    print(f"=== {name} ===")
    print(f"Pixel 1: {p1}, Pixel 2: {p2}")
    print(f"Euclidean Distance  : {d_euc:.4f}")
    print(f"City-Block (D4)     : {d_4}")
    print(f"Chessboard (D8)     : {d_8}\n")