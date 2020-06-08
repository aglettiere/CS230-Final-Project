import sys
import glob 
import os
import cv2
import numpy as np
rootdir = '/home/ubuntu/Dance_data/rgb/generated'
rootdir2 = '/home/ubuntu/Dance_data/rgb/moco/dance'
'''videonum = 0
for image in os.listdir(os.path.join(rootdir, 'generatedballet')):
    os.system("mkdir ./generated/genballet/video" + str(videonum)) 
    for count in range(32):
        img = cv2.imread(os.path.join(rootdir, 'generatedballet', image))
        img_resized = cv2.resize(img, (2048, 64))
        print(img_resized.shape)
        crop = img_resized[0:64, 64 * count: 64 * (count + 1)]
        cv2.imwrite('/home/ubuntu/Dance_data/rgb/generated/genballet/video' + str(videonum) + '/' + str(count) + '.jpg', crop)
    videonum+=1'''

'''for video in os.listdir(os.path.join(rootdir, 'genballet')):
    img_array = []
    for image in glob.glob('/home/ubuntu/Dance_data/rgb/generated/genballet/' + video + '/*.jpg'):
        img = cv2.imread(image)
        height, width, layers = img.shape
        size = (width,height)
        img_array.append(img)
    out = cv2.VideoWriter(video + '.mp4',cv2.VideoWriter_fourcc(*'DIVX'), 10, size)
    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()'''

'''categories = ['concatflamenco', 'concatlatin', 'concatrumba', 'concattango', 'concatbreak', 'concatfoxtrot',
              'concatpasodoble', 'concatsquare', 'concattap', 'concatcha', 'concatjive', 'concatquickstep',
              'concatswing', 'concatwaltz']'''

if __name__=='__main__':
    dance = sys.argv[1]
    os.system("mkdir ../../Inception-Score/data/" + dance)
    print("writing to..." + dance)
    imgnum = 0
    for image in glob.glob('/home/ubuntu/Dance_data/rgb/generated/motion/' + dance + '/*.png'):
        for count in range(16):
            img = cv2.imread(image)
            img_resized = cv2.resize(img, (1024, 64))
            crop = img_resized[0:64, 64 * count: 64 * (count + 1)]
            cv2.imwrite('/home/ubuntu/Inception-Score/data/' + dance + '/img' + str(imgnum) + '.png', crop)
            imgnum+=1
            if(imgnum % 100 == 0): print(imgnum)

'''imgnum = 0
for image in glob.glob('/home/ubuntu/Dance_data/rgb/generated/generatedall/' + '*.png'):
    for count in range(16): 
        img = cv2.imread(image)
        img_resized = cv2.resize(img, (1024, 64))
        crop = img_resized[0:64, 64 * count: 64 * (count + 1)]
        cv2.imwrite('/home/ubuntu/Inception-Score/data/genall/img' + str(imgnum) + '.png', crop)
        imgnum+=1'''
   
