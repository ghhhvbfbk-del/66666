
import  cv2
import matplotlib.pyplot as plt
image =cv2.imread("2.jpg.")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

_, binary = cv2.threshold(gray, 135, 255, cv2.THRESH_BINARY)


contours,  hierarchy =  cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
image  = cv2.drawContours(image, contours, -1,( 0,  255, 0), 1 )
plt.imshow(image)
plt.show()