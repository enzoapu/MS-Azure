# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 19:07:20 2019

@author: Administrator
"""

import cv2






# 選擇第二隻攝影機
cap = cv2.VideoCapture(0)

while(True):
  # 從攝影機擷取一張影像
  ret, frame = cap.read()

  # 顯示圖片
  frame = cv2.flip(frame,1,dst=None) #水平镜像
  cv2.imshow('frame', frame)

  # 若按下 q 鍵則離開迴圈
  if cv2.waitKey(1) & 0xFF == ord('q'):
      cv2.imwrite('img.jpg', frame)
      break

# 釋放攝影機
cap.release()

# 關閉所有 OpenCV 視窗
cv2.destroyAllWindows()
''''''
img = cv2.imread('apu01.jpg')
cv2.imshow('My Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
