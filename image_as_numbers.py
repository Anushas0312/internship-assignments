import cv2
import numpy as np

# Load image (make sure image is in same folder)
image = cv2.imread("sample.jpg")

# Check if image loaded
if image is None:
    print("Error: Image not found!")
else:
    print("Image Loaded Successfully\n")

    # Shape of image
    print("Image Shape (Height, Width, Channels):", image.shape)

    # Pixel values at a point
    print("\nPixel Value at (0,0):", image[0, 0])

    # First row pixel values (partial)
    print("\nFirst Row Pixel Values (first 5 pixels):")
    print(image[0, :5])

    # Number of channels
    print("\nNumber of Channels:", image.shape[2])

    # Explanation
    print("\nExplanation:")
    print("Height = number of rows (pixels vertically)")
    print("Width = number of columns (pixels horizontally)")
    print("Channels = 3 (Blue, Green, Red in OpenCV)")