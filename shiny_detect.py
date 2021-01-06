import cv2
import numpy as np
import datetime
import pytesseract
from time import sleep
from numbermove import Autocar

def shiny_check():
	shiny = "0"
	video = cv2.VideoCapture(2, cv2.CAP_DSHOW)
	# fourcc = cv2.VideoWriter_fourcc(*'X264')
	# out = cv2.VideoWriter('shiny.mp4', fourcc, 20.0, (1280, 720))
	# video = cv2.VideoCapture("shiny.mp4")
	while(video.isOpened()):
		t3 = datetime.datetime.now()
		sleep(0.05)

		ret, img = video.read()
		m1 = cv2.resize(img, (1280, 720))
		m2 = m1[250:500,805:1068]
		m3 = m1[520:580,120:500]
		m1 = m1[250:500,805:1068]
		# m2 = img[280:520,805:1058]
		# m1 = img[280:520,805:1058]

		text = pytesseract.image_to_string(m3, lang='chi_tra')
		if "妙蛙花" not in text:
			m1 = cv2.inRange(m1, (240,240,240),(255,255,255))
			m1 = cv2.dilate(m1, np.ones((30,23)))
			z, a, b = cv2.findContours(m1, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
			cv2.imshow('img', img)
			cv2.imshow('m1', m1)
			cv2.imshow('m2', m2)
			cv2.imshow('m3', m3)
			# out.write(img)
			if cv2.waitKey(15) != -1 or len(a) > 5 or t3 >= t2:
				print(len(a))
				shiny = "1"
				cv2.imwrite("z1.jpg", m2)
				cv2.imwrite("z.jpg", m1)
				cv2.imwrite("z2.jpg", img)
				cv2.imwrite("z3.jpg", m3)
				t3 = datetime.datetime.now()
				print("t3 = ", t3)
				break
		else:
			print("已偵測到派出我方Pokemon，故結束重新刷閃！！")
			break
	video.release()
	# out.release()
	cv2.destroyAllWindows()
	print("shiny = ", shiny)
	return shiny

Car = Autocar()

carStart = datetime.datetime.now()
carClose = carStart + datetime.timedelta(hours = 4 ,minutes = 0)
print("Start = ",carStart)
print("Close = ",carClose)

count = 1
while True:
	check = "0"
	NowTime = datetime.datetime.now()
	if NowTime < carClose:
		Car.go_shiny()
		t1 = datetime.datetime.now()
		t2 = t1 + datetime.timedelta(seconds = 15)
		check = shiny_check()
		if check == "1":
			print("check : ", f"共執行 {count} 次遇到色違！！")
			print("=============================================")
			break
		else:
			print("check : ", f"共執行 {count} 次都沒有遇到！！")
			print("=============================================")
			count += 1
			Car.closegame()
			Car.openGame()
	else:
		break

Car.connectionclose()