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
1. 【 Video Capture Device 】

 	I use HDMI→USB video capture card as my Switch's video input.
  
   ![alt text](https://raw.githubusercontent.com/ahoucbvtw/RegiFamily_shiny/master/Picture/VideoCaptureDevice.png "Video Capture Device")

2. 【 Record videos ： [**Video_save.py**](https://github.com/ahoucbvtw/RegiFamily_shiny/blob/master/Video_save.py) 】

	I use Video Capture Device as my Switch's video input, and use **cv2.VideoWriter_fourcc** to save videos. 
    
    Because of I saved the video as MP4,  **openh264-1.7.0-win64.dll**  this file was necessary.
  
   [**openh264 Download here**](https://github.com/cisco/openh264/releases)
   
3. 【 Save Pictures from videos ： [**Pictures_save.py**](https://github.com/ahoucbvtw/RegiFamily_shiny/blob/master/Pictures_save.py) 】
	
	Set how frequency to get pictures and take frames to numpy array from videos.
    
    According to I discovered the cave's light (background) was different in morning and night, I decided to gather all the morning and night pictures to enhance my identity rate.
    
    ![alt text](https://raw.githubusercontent.com/ahoucbvtw/RegiFamily_shiny/master/Picture/Morning_vs_night.jpg "Morning vs Night")
  
   - Shiny RegiFamily
   
   - NotShiny RegiFamily