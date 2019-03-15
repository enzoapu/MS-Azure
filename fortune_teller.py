# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 19:07:20 2019

@author: Administrator
"""

import cognitive_face as CF
file_path = 'picture.jpg'

KEY = '****************'  # Replace with a valid Subscription Key here.
CF.Key.set(KEY)

BASE_URL = 'https://japaneast.api.cognitive.microsoft.com/face/v1.0/'  # Replace with your regional Base URL
CF.BaseUrl.set(BASE_URL)

img_url = 'https://raw.githubusercontent.com/Microsoft/Cognitive-Face-Windows/master/Data/detection1.jpg'
result = CF.face.detect(file_path,attributes='age,gender,emotion')
print(result)
print("目測有",len(result),"張臉")


while(True):
    
    a = input("算婚姻: ")
    
    if a=='q':
        break
    else:  
        i = int(a)
        gender = result[i]["faceAttributes"]["gender"]
        age = result[i]["faceAttributes"]["age"]
        emotion = result[i]["faceAttributes"]["emotion"]
        
        print('')
        #print('性別: ',gender)
        #print('目測年齡: ',age)
        if gender=='male':
            pred_min = 29-age
            pred_max = 33-age
            print('先生，您',pred_min,'~',pred_max,'年後就會結婚了！')
        elif gender=='female':
            pred_min = 27-age
            pred_max = 31-age
            print('小姐，您',pred_min,'~',pred_max,'年後就會結婚了！')
        
        print('')
        
        import cv2
        img = cv2.imread(file_path)
        #print(img.shape)
        
        width = result[i]["faceRectangle"]["width"]
        height = result[i]["faceRectangle"]["height"]
        left = result[i]["faceRectangle"]["left"]
        top = result[i]["faceRectangle"]["top"]
        # 在圖片上畫一個綠色方框，線條寬度為 2 px
        cv2.rectangle(img, (left, top), (left+width, top+height), (0, 255, 0), 2)
        cv2.imshow('face'+a, img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
