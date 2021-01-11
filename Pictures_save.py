import cv2
import datetime
import os

def get_images_from_video(video_path, time_Frame):
	video_images = []
	video = cv2.VideoCapture(video_path)
	c = 1

	if video.isOpened(): # check the video is opened
		ret, video_frame = video.read()
	else:
		ret = False

	while ret:   # capture the pictures until video is over
		ret, video_frame = video.read()

		if(c % time_Frame == 0): # setting frames to per picture
			video_images.append(video_frame)
		c = c + 1
	video.release()

	return video_images

def save_image(video_images,path,video_name):
	print(f"{video_name}.mp4 共擷取 {len(video_images)} 圖片！！")
	for i in range(0, len(video_images)): # show the all save picture
		try:
			pic_name = f"{path}/{video_name}_{i}.jpg"
			cv2.imwrite(pic_name, video_images[i])
			print(f"{pic_name}>>>儲存成功")
		except:
			pass


Frame = 1
x = "mp4 file"
video_path = f'./{x}'
video_name = x.split(".")[0]
savepath = "savepath"
video_images = get_images_from_video(video_path, Frame) # take each setted frame from picture
save_image(video_images, savepath, video_name)