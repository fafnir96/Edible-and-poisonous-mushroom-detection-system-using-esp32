import cv2
import urllib.request
import numpy as np
import time
from ultralytics import YOLO
import os

# Load YOLO model
model = YOLO(f"{os.getcwd()}/best.pt")

# ESP32-CAM URL
url = 'http://192.168.1.19/cam-hi.jpg'

# Read and display video frames from ESP32-CAM with YOLO detection
def stream_video(url):
    cv2.namedWindow("ESP32-CAM Stream", cv2.WINDOW_AUTOSIZE)

    while True:
        try:
            # Read image from ESP32-CAM
            img_resp = urllib.request.urlopen(url)
            img_np = np.array(bytearray(img_resp.read()), dtype=np.uint8)
            img = cv2.imdecode(img_np, -1)

            if img is not None:
                # YOLO detection
                results = model(img, conf=0.8)
                for result in results:
                    boxes = result.boxes
                    for box in boxes:
                        x1, y1, x2, y2 = box.xyxy.tolist()[0]
                        c = box.cls
                        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                        label = model.names[int(c)]
                        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
                        cv2.putText(img, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

                cv2.imshow("ESP32-CAM Stream", img)

            if cv2.waitKey(5) & 0xFF == ord('q'):
                break

        except urllib.error.HTTPError as e:
            print(f"HTTP Error: {e.code} - {e.reason}")
            time.sleep(1)
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(1)

    cv2.destroyAllWindows()

if __name__ == "__main__":
    stream_video(url)
