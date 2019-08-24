from PIL import Image
import matplotlib.pyplot as plt
import cv2

img1 = cv2.imread('./1.png')
img2 = cv2.imread('./2.png')
img3 = cv2.imread('./3.png')
img4 = cv2.imread('./4.png')
img5 = cv2.imread('./5.png')
img6 = cv2.imread('./6.png')
img7 = cv2.imread('./7.png')
img8 = cv2.imread('./8.png')
img9 = cv2.imread('./9.png')
img10 = cv2.imread('./10.png')
img11and13 = cv2.imread('./11and13.png')
img12 = cv2.imread('./12.png')
img14 = cv2.imread('./14.png')
img15= cv2.imread('./15.png')
img16 = cv2.imread('./16.png')
img17 = cv2.imread('./17.png')
imgTest1 = cv2.imread('./test1.png')
imgTest2 = cv2.imread('./test2.png')
# imgList = [img1,img2,img3,img4,img5,img6,img7,img8,img9,img10,img11and13,img12,img14,img15,img16,img17,imgTest1,imgTest2]
# fig = plt.figure(figsize=(250*6,400*3),dpi=1)
#
# def matplotlib_multi_pic1():
#     for i in range(len(imgList)):
#         # title = 'pic' + str(i+1)
#         plt.subplot(3,6,i+1)
#         img = cv2.resize(imgList[i],(250,400))
#         plt.imshow(img)
#         plt.axis('off')
#
#     plt.show()



imgList = [img1,img2,img3]
fig = plt.figure(figsize=(250*3,300),dpi=1)

img = cv2.resize(imgList[0], (300, 400))
plt.subplot(131)
plt.imshow(img)
plt.axis('off')

img = cv2.resize(imgList[1], (300, 400))
plt.subplot(132)
plt.imshow(img)
plt.axis('off')


plt.show()
#
# def matplotlib_multi_pic1():
#     for i in range(len(imgList)):
#         plt.subplot(1,3,i+1)
#         img = cv2.resize(imgList[i],(250,400))
#         plt.imshow(img)
#         plt.axis('off')
#
#     plt.show()
#
# matplotlib_multi_pic1()
