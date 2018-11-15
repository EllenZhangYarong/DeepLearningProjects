import cv2
import numpy as np

image = cv2.imread('images/bunchofshapes.jpg')
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cv2.imshow('0 - Original Image', image)
cv2.waitKey(0)

blank_image = np.zeros((image.shape[0], image.shape[1], 3))
orginal_image = image_gray


edged_image = cv2.Canny(orginal_image, 50, 200)
cv2.imshow('1 - edged_image', edged_image)
cv2.waitKey(0)

_, contours,hierarchy = cv2.findContours(edged_image.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
print("Number of contours found = ", len(contours))

cv2.drawContours(blank_image,contours, -1, (0,255,0), 3)
cv2.imshow('2 - All Contours over blank image', blank_image)
cv2.waitKey(0)

cv2.drawContours(orginal_image,contours, -1, (0,255,0), 3)
cv2.imshow('3 - All Contours', orginal_image)
cv2.waitKey(0)

cv2.destroyAllWindows()



