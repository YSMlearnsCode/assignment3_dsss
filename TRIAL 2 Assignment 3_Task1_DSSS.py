import matplotlib.pyplot as plt
import random
import imageio as io
from pathlib import Path
import glob
import skimage.io
import json

BAGLS_path = "Mini_BAGLS_dataset"
pathlib_path = Path(BAGLS_path)

# Get all segmentation files
all_seg_files = glob.glob(str(pathlib_path / "*_seg.png"))

# Shuffle the list and select 4 random files
random.shuffle(all_seg_files)
selected_seg = all_seg_files[:4]

# Display 4 images with their segmentation masks and titles from metadata
for i in range(4):
    # Load the original image and segmentation mask
    img_path = selected_seg[i].replace("_seg.png", ".png")
    seg_path = selected_seg[i]
    
    # Read the images
    img = skimage.io.imread(img_path)
    seg = skimage.io.imread(seg_path)
    
    # Load the corresponding metadata file
    meta_path = selected_seg[i].replace("_seg.png", ".meta")
    title = "Unknown status"  # Default title
    if Path(meta_path).exists():
        with open(meta_path, "r") as meta_file:
            meta_data = json.load(meta_file)
            title = meta_data.get("Subject disorder status", "Unknown status")
    
    # Display the original image and segmentation mask
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

    # Display original image with metadata title
    ax1.imshow(img)
    ax1.axis("off")
    ax1.set_title(f"Original Image\nStatus: {title}")

    # Display segmentation mask with label
    ax2.imshow(seg)
    ax2.axis("off")
    ax2.set_title("Segmentation Mask")

    plt.show()