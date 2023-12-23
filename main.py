# let's start with the Imports
import cv2
import numpy as np

#Configurable Parameters
source="bird.jpg"
destination='New Image.jpg'
#destination='New Image.jpeg'
#destination='New Image.png'

# Read the image using imread function
image = cv2.imread(source)
cv2.imshow('Original Image', image)
cv2.waitKey()  # Wait for a key press to close the window

# let's scale the image using new width and  new height
new_width = int(input("Enter the new_width: "))
new_height = int(input("Enter the new_height: "))
new_points = (new_width, new_height)
resized_image = cv2.resize(image, new_points, interpolation=cv2.INTER_LINEAR)

# Display images
cv2.imshow('Resized image by defining height and width', resized_image)
cv2.waitKey()  # Wait for a key press to close the window
cv2.imwrite(destination, resized_image)

# so this is how we resize the image using cv2 opencv-python module.