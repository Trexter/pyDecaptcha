import numpy
import cv2
import time

print("Automatic Apple ID Creator")

index = 1

while index < 23:

	path = "captcha/captcha" + str(index) + ".jpg"

	img = cv2.imread(path)
	gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	

	cv2.imshow('Image', gray_img)
	key = cv2.waitKey(113)
	time.sleep(0.25)
	
	cv2.destroyAllWindows()
	index = index + 1
