import numpy
import cv2
import time
import pytesser

print "Automatic Apple ID Creator\n"

index = 24

while index < 26:

	path = "captcha/captcha" + str(index) + ".jpg"

	img = cv2.imread(path)
	gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	#detect text in the image
	text = pytesser.mat_to_string(gray_img)

	print(text)

	cv2.imshow('Image', gray_img)
	key = cv2.waitKey(113)
	time.sleep(0.25)
	
	cv2.destroyAllWindows()
	index = index + 1
