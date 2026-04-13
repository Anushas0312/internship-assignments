import cv2

# Load image
image = cv2.imread("sample.jpg")

if image is None:
    print("Error: Image not found!")
else:
    print("Image Loaded Successfully")

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply blur
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Edge detection
    edges = cv2.Canny(blur, 100, 200)

    # Show images
    cv2.imshow("Original Image", image)
    cv2.imshow("Grayscale Image", gray)
    cv2.imshow("Blurred Image", blur)
    cv2.imshow("Edge Detection", edges)

    cv2.waitKey(0)
    cv2.destroyAllWindows()