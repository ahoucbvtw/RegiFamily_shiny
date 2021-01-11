import cv2

video = cv2.VideoCapture(2, cv2.CAP_DSHOW)

fourcc = cv2.VideoWriter_fourcc(*'X264')
out = cv2.VideoWriter("377.mp4", fourcc, 20.0, (1280, 720))

while(video.isOpened()):

	ret, img = video.read()
	m2 = cv2.resize(img, (1280, 720))
	out.write(m2)
	cv2.imshow('Video', m2)

	if cv2.waitKey(30) != -1:
		break

video.release()
out.release()
cv2.destroyAllWindows()