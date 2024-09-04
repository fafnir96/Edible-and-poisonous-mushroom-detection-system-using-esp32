# Edible and poisonous mushroom detection system using ESP32-CAM

## Demo Video
[Link](https://drive.google.com/file/d/1qsBZPDFAnRhWENG6cRLUC8VeuEWVgjO5/view?usp=drive_link)

## Purpose
The purpose of this research is to design and develop a toxic and non-toxic mushroom detection system using the ESP32-CAM, leveraging YOLOv8 object detection technology. This system aims to provide a practical solution for real-time mushroom identification, helping to differentiate between toxic and non-toxic mushrooms to enhance user safety. The primary objectives of this system are:

1. Accurately Identify Mushrooms: Utilize the YOLOv8 object detection model to train the system in identifying both toxic and non-toxic mushrooms with high accuracy. The dataset used will include relevant images of mushrooms for model training.
2. Integration with ESP32-CAM: Integrate the YOLOv8 object detection model with the ESP32-CAM to enable real-time image capture and processing on the device. The system should be capable of processing and analyzing mushroom images directly through the ESP32-CAM's camera.


## Setup
1. Clone project
2. Open file static-IP-ESP32CAM.ino in Arduino IDE
3. Upload file static-IP-ESP32CAM.ino to ESP32-CAM
4. Open project in VSCode
5. Create a virtual environment: `python -m venv myvenv`
6. Activate virtual environment: `\myvenv\Scripts\activate`
7. Install ultralytics package: `pip install ultralytics`
8. Change the url in code to url ESP32-CAM
9. Run Python scripts `jamur.py` 
