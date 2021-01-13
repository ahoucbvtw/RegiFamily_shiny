# RegiFamily Shiny or NotShiny

I was build a simple CNN to identify the **Legendary Titans**：**Regirock**, **Registeel**, **Regice**, **Regieleki**,  **Regidrago** these 5 pokemons  in Switch Game Pokemon Sword and Shield.

Then use this model to encounter their shiny type automatically.

**Result_NotShiny：**

![alt text](https://raw.githubusercontent.com/ahoucbvtw/RegiFamily_shiny/master/Picture/Result_377_NotShiny_morning0.jpg "Not Shiny Regirock！！")

**Result_Shiny：**

![alt text](https://raw.githubusercontent.com/ahoucbvtw/RegiFamily_shiny/master/Picture/ShinyResult_377.jpg "Shiny Regirock！！")

## List

- **[Requirements](https://github.com/ahoucbvtw/RegiFamily_shiny#requirements)**
- **[Make Training Pictures](https://github.com/ahoucbvtw/RegiFamily_shiny#make-training-pictures)**
- **[Training](https://github.com/ahoucbvtw/RegiFamily_shiny#training)**
- **[Demo Video](https://github.com/ahoucbvtw/RegiFamily_shiny#demo-video)**


## Requirements

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

## Make Training Pictures
1. 【 Video Capture Device 】

 	I use HDMI→USB video capture card as my Switch's video input.
  
  ![Video Capture Card](https://raw.githubusercontent.com/ahoucbvtw/RegiFamily_shiny/master/Picture/VideoCaptureDevice.png)

2. 【 Record videos ： [**Video_save.py**](https://github.com/ahoucbvtw/RegiFamily_shiny/blob/master/Video_save.py) 】

	I use Video Capture Device as my Switch's video input, and use **cv2.VideoWriter_fourcc** to save videos. 
    
    Because of I saved the video as MP4,  **openh264-1.7.0-win64.dll**  this file was necessary.
  
   [**openh264 Download here**](https://github.com/cisco/openh264/releases)
   
3. 【 Save Pictures from videos ： [**Pictures_save.py**](https://github.com/ahoucbvtw/RegiFamily_shiny/blob/master/Pictures_save.py) 】
	
	Set how frequency to get pictures and take frames to numpy array from videos.
    
    According to I discovered the cave's light (background) was different in morning and night, I decided to gather all the morning and night pictures to enhance my identity rate.
    
    ![alt text](https://raw.githubusercontent.com/ahoucbvtw/RegiFamily_shiny/master/Picture/Morning_vs_night.jpg "Morning vs Night")
  
   - **Shiny RegiFamily**
   
     Because of I never encounter the shiny RegiFamily, I found the shiny RegiFamily from YouTube as my Training pictures.
   
   - **NotShiny RegiFamily**
   
     I recorded all the RegiFamily normal color with Video Capture Device morning and night the time in the game.
     
     Then the frame was setted 1 when I was saved training pictures.
    
## Training

I build two models and the Dence layers was the same but convolutional layers was different for training.

First was use Transfer Learning (VGG16), second was slef-build convolutional layers. Use these two models to compare witch one is more simple, fast, high accuracy.

According to the result, the VGG16 is the best model in this project.

Why not try more other famous models？ The reason is use VGG16 to identify this project is enough. In actual fact, its identity rate was vary high even closed to 100% when I was used.

**Regirock** training loss & accuracy ：

![alt text](https://raw.githubusercontent.com/ahoucbvtw/RegiFamily_shiny/master/Picture/VGG16_377_loss1.png "Regirock Training & Validation Loss")
![alt text](https://raw.githubusercontent.com/ahoucbvtw/RegiFamily_shiny/master/Picture/VGG16_377accuracy.png "Regirock Training & Validation Accuracy")

**Regice** training loss & accuracy ：

![alt text](https://raw.githubusercontent.com/ahoucbvtw/RegiFamily_shiny/master/Picture/VGG16_378_loss1.png "Regice Training & Validation Loss")
![alt text](https://raw.githubusercontent.com/ahoucbvtw/RegiFamily_shiny/master/Picture/VGG16_378accuracy.png "Regice Training & Validation Accuracy")

**Registeel** training loss & accuracy ：

![alt text](https://raw.githubusercontent.com/ahoucbvtw/RegiFamily_shiny/master/Picture/VGG16_379loss1.png "Registeel Training & Validation Loss")
![alt text](https://raw.githubusercontent.com/ahoucbvtw/RegiFamily_shiny/master/Picture/VGG16_379accuracy1.png "Registeel Training & Validation Accuracy")

But Regice is different. Other RegiFamily's shiny type has large of difference from normal type, only Regice's two of types are vary close, even human eyes can not identify without any information.

![alt text](https://raw.githubusercontent.com/ahoucbvtw/RegiFamily_shiny/master/Picture/RegiFamily%20Shiny%20vs%20NotShiny.png "RegiFamily Shiny vs NotShiny")

Thus, I use image process to catch definitely appeared the shiny light when encountered shiny Pokemon. → **[shiny_detect.py](https://github.com/ahoucbvtw/RegiFamily_shiny/blob/master/shiny_detect.py/)**

I use **cv2.inRange** to catch the ShinyLight, and use **cv2.dilate** to make my target more cleary, then use **cv2.findContours** to find the contour point and count it. 

If the ShinyLight contour point is more than 6 even 8, it must be encounterd the shiny Regice certainly.

```
m1 = cv2.inRange(m1, (240,240,240),(255,255,255))
m1 = cv2.dilate(m1, np.ones((30,23)))
z, a, b = cv2.findContours(m1, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
```

![alt text](https://raw.githubusercontent.com/ahoucbvtw/RegiFamily_shiny/master/Picture/Result_OpenCV_378_ShinyLight.jpg "ShinyLight Contour Point")
![alt text](https://raw.githubusercontent.com/ahoucbvtw/RegiFamily_shiny/master/Picture/Result_OpenCV_378_Shiny.jpg "Shiny Regice！！")

![alt text](https://raw.githubusercontent.com/ahoucbvtw/RegiFamily_shiny/master/Picture/378shiny_log.jpg "Encounter Shiny Regice's Log")

## Demo Video

- **CNN (VGG16)**

  - **Regirock Auto Shiny Farming ：**

    [![d](https://raw.githubusercontent.com/ahoucbvtw/RegiFamily_shiny/master/Picture/377_Auto_Shiny_Farming.jpg)](http://www.youtube.com/watch?v=v_71KjZrdEY "377 Regirock Auto Shiny Farming Use CNN")
    
  - **Registeel Auto Shiny Farming ：**
  
    [![d](https://raw.githubusercontent.com/ahoucbvtw/RegiFamily_shiny/master/Picture/379_Auto_Shiny_Farming.jpg)](https://www.youtube.com/watch?v=YQHtD1ixFeM "379 Registeel Auto Shiny Farming Use CNN")
    
- **Image Process (OpenCV)**

  - **Regice Auto Shiny Farming ：**

    [![d](https://raw.githubusercontent.com/ahoucbvtw/RegiFamily_shiny/master/Picture/378_Auto_Shiny_Farming.jpg)](https://www.youtube.com/watch?v=auTGc-Dpkzk "378 Regice Auto Shiny Farming Use Image Process")