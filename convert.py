import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm # For progress bars
import re 
# === CONFIGURATION ===
# Set the new target size
TARGET_SIZE = 200

# Define your dataset paths
# Assuming your structure is something like:
# ProjectFolder/
# ├── Dataset/
# │   ├── photos/
# │   │   ├── image1.jpg
# │   │   ├── image2.jpg
# │   └── sketches/
# │       ├── sketch1.jpg
# │       ├── sketch2.jpg
# └── your_script.py
image_dataset_path = "Dataset/photos"
sketch_dataset_path = "Dataset/sketches"

# === HELPER FUNCTIONS ===

def sorted_alphanumeric(data):
    """Sort filenames properly (useful for matching pairs if needed later)."""
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(data, key=alphanum_key)

def load_and_resize_image(filepath, size=200):
    """
    Load an image, convert BGR to RGB, and resize it to the specified dimensions.
    Returns the resized image as a NumPy array (uint8) or None if loading fails.
    """
    image = cv2.imread(filepath)
    if image is None:
        print(f"Warning: Unable to load image {filepath}. Skipping.")
        return None
    # Convert BGR (OpenCV default) to RGB for consistent plotting/processing
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # Resize the image to the target size
    image = cv2.resize(image, (size, size))
    return image # Image is still in uint8 format (0-255), not normalized yet


# === DATA LOADING AND RESIZING ===

resized_photos_array = []
resized_sketches_array = []

# Ensure the dataset directories exist before proceeding
if not os.path.exists(image_dataset_path):
    print(f"Error: Photo dataset path '{image_dataset_path}' does not exist.")
    # You might want to create dummy directories and files for testing,
    # or prompt the user to create them. For now, we'll exit.
    # --- For demonstration, creating dummy files ---
    print("Creating dummy dataset folders and images for demonstration...")
    os.makedirs(image_dataset_path, exist_ok=True)
    os.makedirs(sketch_dataset_path, exist_ok=True)
    for i in range(3): # Create 3 dummy photo and sketch pairs
        # Create a dummy photo (e.g., 300x300 blue image)
        dummy_photo = np.zeros((300, 300, 3), dtype=np.uint8)
        dummy_photo[:, :, 2] = 255 # Blue channel
        cv2.imwrite(os.path.join(image_dataset_path, f'photo_{i+1}.jpg'), cv2.cvtColor(dummy_photo, cv2.COLOR_RGB2BGR))

        # Create a dummy sketch (e.g., 150x150 green image)
        dummy_sketch = np.zeros((150, 150, 3), dtype=np.uint8)
        dummy_sketch[:, :, 1] = 255 # Green channel
        cv2.imwrite(os.path.join(sketch_dataset_path, f'sketch_{i+1}.jpg'), cv2.cvtColor(dummy_sketch, cv2.COLOR_RGB2BGR))
    print("Dummy dataset created. Please replace with your actual data.")
    # --- End of dummy creation ---
    # In a real scenario, you might raise an error or sys.exit(1) here.


print(f"Resizing all images to {TARGET_SIZE}x{TARGET_SIZE} pixels.")

# Process photos
photo_filenames = sorted_alphanumeric(os.listdir(image_dataset_path))
print(f"Found {len(photo_filenames)} photos in '{image_dataset_path}'.")

for filename in tqdm(photo_filenames, desc="Resizing Photos"):
    filepath = os.path.join(image_dataset_path, filename)
    resized_img = load_and_resize_image(filepath, size=TARGET_SIZE)
    if resized_img is not None:
        resized_photos_array.append(resized_img)

# Process sketches
sketch_filenames = sorted_alphanumeric(os.listdir(sketch_dataset_path))
print(f"Found {len(sketch_filenames)} sketches in '{sketch_dataset_path}'.")

for filename in tqdm(sketch_filenames, desc="Resizing Sketches"):
    filepath = os.path.join(sketch_dataset_path, filename)
    resized_img = load_and_resize_image(filepath, size=TARGET_SIZE)
    if resized_img is not None:
        resized_sketches_array.append(resized_img)

# === FINAL CHECK AND CONVERSION TO NUMPY ARRAYS ===

print(f"\nTotal number of resized photos: {len(resized_photos_array)}")
print(f"Total number of resized sketches: {len(resized_sketches_array)}")

# Convert lists to NumPy arrays
final_photos_array = np.array(resized_photos_array)
final_sketches_array = np.array(resized_sketches_array)

print(f"Shape of the final photos array: {final_photos_array.shape}")
print(f"Shape of the final sketches array: {final_sketches_array.shape}")

# === PLOT SAMPLE ===

def plot_sample_images(photos_arr, sketches_arr):
    """Plots a random pair of resized photo and sketch."""
    if not photos_arr.shape[0] or not sketches_arr.shape[0]:
        print("No images to display. Arrays are empty.")
        return

    # Find the minimum number of images to ensure we can pick a valid index
    min_len = min(photos_arr.shape[0], sketches_arr.shape[0])
    if min_len == 0:
        print("Not enough images in arrays to plot a sample.")
        return

    idx = np.random.randint(0, min_len)

    plt.figure(figsize=(8, 4))

    plt.subplot(1, 2, 1)
    plt.imshow(photos_arr[idx])
    plt.title(f'Resized Photo ({photos_arr[idx].shape[0]}x{photos_arr[idx].shape[1]})')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(sketches_arr[idx])
    plt.title(f'Resized Sketch ({sketches_arr[idx].shape[0]}x{sketches_arr[idx].shape[1]})')
    plt.axis('off')

    plt.suptitle(f"Sample Resized Images (Index: {idx})")
    plt.show()

# Example: plot a random sample from the resized arrays
plot_sample_images(final_photos_array, final_sketches_array)

# You can now save these arrays if needed:
# np.save('/kaggle/working/resized_photos.npy', final_photos_array)
# np.save('/kaggle/working/resized_sketches.npy', final_sketches_array)
# print("Resized arrays saved successfully!")
