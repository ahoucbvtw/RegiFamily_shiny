import numpy as np
import cv2
import pytesseract
import datetime
from numbermove import Autocar
from tensorflow.keras.models import load_model

trans = ["沒閃", "閃"]
model = load_model("379.h5")

def shinny_check():

	video = cv2.VideoCapture(0, cv2.CAP_DSHOW)
	while(video.isOpened()):
		t3 = datetime.datetime.now()
		answer= "沒閃"
		ret, img = video.read()

		# m3為擷取遇到野生怪時下方的對話框文字使用
		m3 = cv2.resize(img, (1280, 720))
		m3 = m3[550:700,110:450]
		pytesseract.pytesseract.tesseract_cmd = r"C:\Users\jack_\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
		text = pytesseract.image_to_string(m3, lang='chi_tra')
		cv2.imshow('cv2_BGR', img)
		cv2.imshow('m3', m3)

		# 下方文字判斷到"野生"2字才開始做CNN圖形判斷
		if "野生" in text:
			# 因為cv2預設彩色通道讀取為BGR，與當時訓練CNN模型使用的flow_from_directory預設不同
			# 因此需先轉換成RGB
			m1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

			# 31~35行為把每一張frame圖片做預處理轉換成與當時訓練CNN輸入的圖片是一樣
			m1 = cv2.resize(m1, (300, 300))
			image = m1.reshape(1, m1.shape[0], m1.shape[1], m1.shape[2]) / 255
			# print(image)
			# print(image.shape)
			cv2.imshow('cv2_RGB', m1)

			# 38~43行進行模型圖片的判斷
			p = model.predict(image)[0]
			print("==============================")
			for n, prob in zip(trans, p):
				print(n, "的機率:", round(prob, 3))
			print("==============================")
			ans = model.predict_classes(image)[0]
			answer = trans[ans]

			if answer == "沒閃":
				cv2.imwrite("z1.jpg", img)
				print("此次並非閃光！！故重新開機執行！！")
			else:
				cv2.imwrite("z1.jpg", img)
				print("遇到閃光！！")
			break
		if cv2.waitKey(15) != -1 or t3 >= t2:
			print("偵測到提前結束偵測！！")
			break

	video.release()
	cv2.destroyAllWindows()
	return answer

carStart = datetime.datetime.now()
carClose = carStart + datetime.timedelta(hours = 5 ,minutes = 0)
print("Start = ",carStart)
print("Close = ",carClose)

Car = Autocar()

count = 1
while True:
	check = "0"
	NowTime = datetime.datetime.now()
	if NowTime < carClose:
		Car.go_shinny()
		t1 = datetime.datetime.now()
		t2 = t1 + datetime.timedelta(seconds = 15)
		check = shinny_check()
		print("check = ", check)
		if check == "閃":
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