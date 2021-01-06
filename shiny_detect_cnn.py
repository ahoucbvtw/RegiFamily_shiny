import numpy as np
import cv2
import pytesseract
import datetime
from numbermove import Autocar
from tensorflow.keras.models import load_model

model_select = "377.h5"

trans = ["沒閃", "閃"] # model's number answer translate
trans_Eng = ["NotShiny", "Shiny"] # model's number answer translate
model = load_model(model_select)

def shiny_check():

	video = cv2.VideoCapture(0, cv2.CAP_DSHOW)
	while(video.isOpened()):
		t3 = datetime.datetime.now()
		answer = "沒閃"
		ret, img = video.read()

		# m3為擷取遇到野生怪時下方的對話框文字使用
		# m3 is captured the dialog box when encounter a wild Pokemon
		m3 = cv2.resize(img, (1280, 720))
		m3 = m3[550:700,110:450]

		text = pytesseract.image_to_string(m3, lang='chi_tra')
		cv2.imshow('cv2_BGR', img)
		cv2.imshow('text_detect', m3)

		# 下方文字判斷到"野生"2字才開始做CNN圖形判斷
		# Start CNN when if the dialog box detected "wild"
		if "野生" in text:
			# 因為cv2預設彩色通道讀取為BGR，與當時訓練CNN模型使用的flow_from_directory預設不同
			# 因此需先轉換成RGB
			# Because of used "flow_from_directory(RGB)" for training, the color channel is different with cv2(BGR)
			# Use cv2 must to change RGB first, then put in the model to predict
			m1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

			# 38~43行為把每一張frame圖片做預處理轉換成與當時訓練CNN輸入的圖片是一樣
			# 38~43 row is picture preprocessing same as training
			m1 = cv2.resize(m1, (300, 300))
			image = m1.reshape(1, m1.shape[0], m1.shape[1], m1.shape[2]) / 255
			# cv2.imshow('cv2_RGB', m1)

			# 48~59行進行模型圖片的判斷
			# 48~59 row is model predict phase
			p = model.predict(image)[0]
			print("==============================")
			# predict answer for chinese
			for n, prob in zip(trans, p):
				print(n, "的機率:", round(prob, 3))

			# predict answer for english
			for n, prob in zip(trans_Eng, p):
				print(n, "Probability:", round(prob, 3))
			print("==============================")
			ans = model.predict_classes(image)[0]
			answer = trans[ans]

			resultpic_name = model_select.split(".")[0]

			if answer == "沒閃": # if not shiny
				# 新增NotShiny文字
				# add NotShiny text
				text = "NotShiny !!"
				cv2.putText(img, text, (200, 95), cv2.FONT_HERSHEY_PLAIN,3, (0, 255, 255), 3, cv2.LINE_AA)

				# 儲存圖加入文字時用的擷取範圍
				# save result picture
				add_text = img[50:380,80:580]
				cv2.imwrite(f"Result_{resultpic_name}_NotShiny.jpg", add_text)

				print("此次並非閃光！！故重新開機執行！！\nIt's Not Shiny！！Restart The Game Now！！")
			else:
				# 新增Shiny文字
				# add Shiny text
				text = "Shiny !!"
				cv2.putText(img, text, (240, 95), cv2.FONT_HERSHEY_PLAIN,3, (0, 255, 255), 3, cv2.LINE_AA)

				# 儲存圖加入文字時用的擷取範圍
				# save result picture
				add_text = img[50:380,80:580]
				cv2.imwrite(f"Result_{resultpic_name}_Shiny.jpg", add_text)

				print("遇到閃光！！\nCongratulations！！It's Shiny！！")
			break
		if cv2.waitKey(15) != -1 or t3 >= t2:
			print("偵測到提前結束確認！！\nEarly End Is Detected！！")
			break

	video.release()
	cv2.destroyAllWindows()
	return answer

# set the script end time
carStart = datetime.datetime.now()
carClose = carStart + datetime.timedelta(hours = 6 ,minutes = 0)
print("Start = ",carStart)
print("Close = ",carClose)

Car = Autocar()

# script start
count = 1
while True:
	check = "0"
	NowTime = datetime.datetime.now()
	if NowTime < carClose:
		Car.go_shiny()
		t1 = datetime.datetime.now()
		t2 = t1 + datetime.timedelta(seconds = 20) # time limit for prevent screen is freezed when CNN predict
		check = shiny_check()
		print("===================================================")
		print("Check = ", check)
		if check == "閃":
			print("Check : ", f"共執行 {count} 次遇到色違！！")
			print("Check : ", f"Encounter Shiny when Loop {count} times！！")
			print("===================================================")
			break
		else:
			print("Check : ", f"共執行 {count} 次都沒有遇到！！")
			print("Check : ", f"No Shiny when Loop {count} times！！")
			print("===================================================")
			count += 1
			Car.closegame()
			Car.openGame()
	else:
		break

Car.connectionclose()