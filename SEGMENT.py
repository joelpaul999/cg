import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("image.jpeg", cv2.IMREAD_GRAYSCALE)

T = float(np.mean(img))

epsilon = 0.5
max_iterations = 100

for _ in range(max_iterations):

    G1 = img[img > T]
    G2 = img[img <= T]

    if len(G1) == 0 or len(G2) == 0:
        break

    m1 = np.mean(G1)
    m2 = np.mean(G2)

    T_new = (m1 + m2) / 2.0

    if abs(T_new - T) < epsilon:
        T = T_new
        break

    T = T_new

segmented_img = np.zeros_like(img)
segmented_img[img > T] = 255
segmented_img[img <= T] = 0

plt.figure(figsize=(8, 4))

plt.subplot(1, 2, 1)
plt.imshow(img, cmap="gray")
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(segmented_img, cmap="gray")
plt.title(f"Segmented Image (T={T:.2f})")
plt.axis("off")

plt.tight_layout()
plt.show()