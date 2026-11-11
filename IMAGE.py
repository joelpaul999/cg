
import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread("image.jpg", cv2.IMREAD_GRAYSCALE)

identity = image.copy()
negative = 255 - image

c = 255 / np.log(1 + np.max(image))
log_transformed = c * np.log(1 + image.astype(np.float32))
log_transformed = np.uint8(log_transformed)

c = 255 / (np.exp(1) - 1)
inv_log_transformed = c * (np.exp(image / 250) - 1)
inv_log_transformed = np.uint8(
    inv_log_transformed * 255 / np.max(inv_log_transformed)
)

gamma = 2.0
power_transformed = np.array(
    255 * (image / 255) ** gamma, dtype="uint8"
)

gamma = 0.5
root_transformed = np.array(
    255 * (image / 255) ** gamma, dtype="uint8"
)

titles = [
    "Original Image",
    "Identity",
    "Negative",
    "Log Transformed",
    "Inverse Log Transformed",
    "Power Transformation",
    "Root Transformation"
]

images = [
    image,
    identity,
    negative,
    log_transformed,
    inv_log_transformed,
    power_transformed,
    root_transformed
]

plt.figure(figsize=(10, 14))

for i in range(len(images)):
    plt.subplot(3, 3, i + 1)
    plt.imshow(images[i], cmap="gray")
    plt.title(titles[i])
    plt.axis("off")

plt.tight_layout()
plt.show()
