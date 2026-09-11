import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

image_rgb = np.array(Image.open("sample.jpg"))
N = 8

downsampled = image_rgb[::N, ::N, :]

pixelated = np.repeat(np.repeat(downsampled, N, axis=0), N, axis=1)

orig_bytes = image_rgb.nbytes
down_bytes = downsampled.nbytes
dim_reduction = (1 - (1 / N)) * 100
mem_savings = ((orig_bytes - down_bytes) / orig_bytes) * 100

print(f"--- DOWNSAMPLING ANALYSIS (N={N}) ---")
print(f"Original Shape:      {image_rgb.shape} | Memory: {orig_bytes:,} bytes")
print(f"Downsampled Shape:   {downsampled.shape} | Memory: {down_bytes:,} bytes")
print(f"Re-expanded Shape:   {pixelated.shape} | Visual: Blocky Pixelation")
print(f"Dimension Reduction: {dim_reduction:.2f}% reduction per axis")
print(f"Memory Savings:      {mem_savings:.2f}% data reduction")

fig, axes = plt.subplots(1, 3, figsize=(14, 5))
axes[0].imshow(image_rgb)
axes[0].set_title(f"Original {image_rgb.shape[:2]}")
axes[1].imshow(downsampled)
axes[1].set_title(f"Downsampled (1/{N}x) {downsampled.shape[:2]}")
axes[2].imshow(pixelated)
axes[2].set_title(f"Re-expanded (Pixelated) {pixelated.shape[:2]}")

for ax in axes:
    ax.axis("off")

plt.tight_layout()
plt.show()