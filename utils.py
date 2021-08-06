import cv2
def  mask(): 
    net_mask = cv2.dnn.readNet("yolov3_mask_last.weights", "yolov3_mask.cfg")
    net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")