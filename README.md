## RegiFamily Shiny or NotShiny
---
I was build a simple CNN to identify the **Legendary Titans**：**Regirock**, **Registeel**, **Regice**, **Regieleki**,  **Regidrago** these 5 pokemons  in Switch Game Pokemon Sword and Shield.

Then use this model to encounter their shiny style automatically.

Result_NotShiny：

![alt text](https://raw.githubusercontent.com/ahoucbvtw/RegiFamily_shiny/master/Picture/Result_377_NotShiny_morning0.jpg "Not Shiny Regirock！！")

Result_Shiny：

![alt text](https://raw.githubusercontent.com/ahoucbvtw/RegiFamily_shiny/master/Picture/ShinyResult_377.jpg "Shiny Regirock！！")

---
### Requirements
- Environment

|| Version & Specification | 
|---------|---------| 
| **OS** | Windows10 |
| **GPU** | GeForce GTX 1050Ti |
| **NVIDIA Driver** | 456.71 - WHQL |
| **Tensorflow-GPU** | 2.3.1 |
| **CUDA & cuDNN** | 10.1 & v7.6.5 |

- Necessary for Python Packages
  - 【**tensorflow-gpu 2.3.1**】
  
    This Package is must important to use GPU for high performance numerical computation.

    **[pypi : tensorflow-gpu](https://pypi.org/project/tensorflow-gpu/)**
    - Install Command : **pip install tensorflow-gpu**

  - 【**pyserial 3.4**】

    This Package can control our **arduino equipment**.

    **[pypi : pyserial](https://pypi.org/project/pyserial/)**
    - Install Command : **pip install pyserial**

  - 【**pytesseract 0.3.6**】

    This Package can let us to Identify the word.

    **[pypi : pytesseract](https://pypi.org/project/pytesseract/)**
    - Install Command : **pip install pytesseract**
    - After pip pytesseract, go to Github and download/install for your PC. → **[UB-Mannheim/tesseract](https://github.com/UB-Mannheim/tesseract/wiki)**
    - Go to installed path to find **tesseract.exe**.  Then add this file's path to your Environment Variable.
  
  - 【**opencv-python 3.4.11.39**】

    This Package can let us to video stream from Switch and image process.

    **[pypi : opencv-python](https://pypi.org/project/opencv-python/)**
    - Install Command : **pip install opencv-python**

  - 【**numpy 1.18.5**】

    This Package is for image process.

    **[pypi : numpy](https://pypi.org/project/numpy/)**
    - Install Command : **pip install numpy**

---
### Make Training Pictures
1. 【Video Capture Card】

 	I use HDMI→USB video capture card as my Switch's video input.
  
  ![Video Capture Card](https://d.ecimg.tw/items/DMAA6NA900APS1A/000001_1592269853.jpg)

2. 【Record videos】

	I recorded videos from Python. Because of I saved the video as MP4,  **openh264-1.7.0-win64.dll**  this file was necessary.
  
   [**openh264 Download here**](https://github.com/cisco/openh264/releases)
   
   ```
	import cv2

	video = cv2.VideoCapture(2, cv2.CAP_DSHOW)

	fourcc = cv2.VideoWriter_fourcc(*'X264')
	out = cv2.VideoWriter(377.mp4', fourcc, 20.0, (1280, 720))

	while(video.isOpened()):

	ret, img = video.read()
	m2 = cv2.resize(img, (1280, 960))
	out.write(m2)
	cv2.imshow('Video', m2)
	
	if cv2.waitKey(30) != -1:
		break
        
	video.release()
	out.release()
	cv2.destroyAllWindows()
    ```
   
3. 【Save Pictures from videos】
	
	Set how frequency to get pictures and take frames to numpy array from videos.
   