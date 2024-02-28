#import libraries
import cv2
import matplotlib.pyplot as plt

#read image
img = cv2.imread('drone.jpeg')

#convert image to RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#plot image
plt.imshow(img)
plt.show()

#convert image to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#plot image
plt.imshow(img_gray, cmap='gray')
plt.show()

#save image
cv2.imwrite('output-image.png', img_gray)