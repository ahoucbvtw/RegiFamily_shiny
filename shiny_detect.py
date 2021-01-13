import cv2
import numpy as np
import datetime
import pytesseract
from time import sleep
from numbermove import Autocar

resultpic_name = "OpenCV_378"

def shiny_check():
	shiny = "0"
	video = cv2.VideoCapture(2, cv2.CAP_DSHOW)
	while(video.isOpened()):
		t3 = datetime.datetime.now()

		ret, img = video.read()
		m1 = cv2.resize(img, (1280, 720))
		m2 = m1[250:500,805:1068]
		m3 = m1[520:580,120:500]
		m1 = m1[250:500,805:1068]

		text = pytesseract.image_to_string(m3, lang='chi_tra')
		# Start detect when if the dialog box detected "go"
		if "去吧" not in text:
			m1 = cv2.inRange(m1, (240,240,240),(255,255,255))
			m1 = cv2.dilate(m1, np.ones((30,23)))
			z, a, b = cv2.findContours(m1, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
			cv2.imshow('img', img)
			cv2.imshow('m1', m1)
			cv2.imshow('m2', m2)
			cv2.imshow('m3', m3)

			if cv2.waitKey(15) != -1 or len(a) > 6 or t3 >= t2:
				print(f"閃光數量 = {len(a)}！！恭喜遇到閃光！！")
				print(f"ShinyLight = {len(a)}！！Congratulations！！It's Shiny！！")
				shiny = "1"
				text = "Shiny !!"
				cv2.imwrite(f"Original_{resultpic_name}_Shiny.jpg", img)
				cv2.imwrite(f"Only_{resultpic_name}_Shiny.jpg", m2)
				cv2.putText(m2, text, (10, 45), cv2.FONT_HERSHEY_PLAIN,3, (0, 255, 255), 3, cv2.LINE_AA)
				cv2.imwrite(f"Result_{resultpic_name}_Shiny.jpg", m2)
				break
			else:
				shiny = "0"

		else:
			print("已偵測到派出我方Pokemon！！故重新開機執行！！")
			print("Detected our Pokemon is on the stage！！Restart The Game Now！！")
			break
	video.release()
	cv2.destroyAllWindows()
	return shiny

Car = Autocar()

carStart = datetime.datetime.now()
carClose = carStart + datetime.timedelta(hours = 12 ,minutes = 0)
print("Start = ",carStart)
print("Close = ",carClose)

count = 1
while True:
	check = "0"
	NowTime = datetime.datetime.now()
	if NowTime < carClose:
		Car.go_shiny()
		t1 = datetime.datetime.now()
		t2 = t1 + datetime.timedelta(seconds = 15) # time limit for prevent screen is freezed when encounter pokemon
		check = shiny_check()
		print("=============================================")
		print("Check = ", check)
		if check == "1":
			print("check : ", f"共執行 {count} 次遇到色違！！")
			print("Check : ", f"Encounter Shiny when Loop {count} times！！")
			print("=============================================")
			break
		else:
			print("check : ", f"共執行 {count} 次都沒有遇到！！")
			print("Check : ", f"No Shiny when Loop {count} times！！")
			print("=============================================")
			count += 1
			Car.closegame()
			Car.openGame()
	else:
		break

Car.connectionclose()