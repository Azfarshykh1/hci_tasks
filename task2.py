import numpy as np

height, width = 300, 400
image = np.zeros((height, width, 3), dtype=np.uint8)

mid_y = height // 2
mid_x = width // 2

image[:mid_y, :mid_x] = [255, 0, 0]      
image[:mid_y, mid_x:] = [0, 255, 0]      
image[mid_y:, :mid_x] = [0, 0, 255]      
image[mid_y:, mid_x:] = [255, 255, 255]  

print("--- SYNTHETIC MATRIX METRICS ---")
print(f"Array Shape (H, W, C): {image.shape}")
print(f"Data Type:             {image.dtype}")
print(f"Total Elements:        {image.size:,} values")
print(f"Memory Footprint:      {image.nbytes:,} bytes ({image.nbytes / 1024:.2f} KB)")