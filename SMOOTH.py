
import cv2
import matplotlib.pyplot as plt
import numpy as np

# Read image in grayscale
img = cv2.imread("image.jpg", cv2.IMREAD_GRAYSCALE)

# Check whether image is loaded
if img is None:
    print("Image not found!")
    exit()

# Create 3x3 kernel
kernel = np.ones((3, 3), np.uint8)

# Apply smoothing filters
img_blur = cv2.blur(img, (5, 5))

img_gaussian = cv2.GaussianBlur(img, (5, 5), 0)

img_box = cv2.boxFilter(img, -1, (5, 5))

img_median = cv2.medianBlur(img, 5)

# Apply morphological operations
img_erode = cv2.erode(img, kernel, iterations=1)

img_dilate = cv2.dilate(img, kernel, iterations=1)

# Apply bilateral filter
img_bilateral = cv2.bilateralFilter(img, 9, 75, 75)

# Store all images
images = [
    img,
    img_blur,
    img_gaussian,
    img_box,
    img_median,
    img_erode,
    img_dilate,
    img_bilateral
]

# Store image titles
titles = [
    "Original",
    "Mean Blur",
    "Gaussian Blur",
    "Box Filter",
    "Median Blur",
    "Eroded",
    "Dilated",
    "Bilateral Filter"
]

# Display all images
plt.figure(figsize=(12, 8))

for i in range(len(images)):
    plt.subplot(2, 4, i + 1)
    plt.imshow(images[i], cmap="gray")
    plt.title(titles[i])
    plt.axis("off")

plt.tight_layout()
plt.show()
