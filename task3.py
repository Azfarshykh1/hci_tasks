import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

img = np.array(Image.open("sample.jpg"))

channels = []
for i in range(3):
    isolated = np.zeros_like(img)
    isolated[:, :, i] = img[:, :, i]
    channels.append((isolated, img[:, :, i]))

fig, axes = plt.subplots(2, 3, figsize=(10, 6))
titles = ["Red", "Green", "Blue"]

for i in range(3):
    axes[0, i].imshow(channels[i][0])
    axes[0, i].set_title(f"{titles[i]} Color")
    axes[1, i].imshow(channels[i][1], cmap="gray")
    axes[1, i].set_title(f"{titles[i]} Gray")
    axes[0, i].axis("off")
    axes[1, i].axis("off")

plt.tight_layout()
plt.show()