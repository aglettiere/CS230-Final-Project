import os
import cv2
import numpy as np
rootdir = '/home/ubuntu/Dance_data/rgb/balletmoco'
folders = os.listdir(rootdir)
count = 0
for f in folders:
	if f == 'concatJPGS.py' and f == 'concatballet':
		break
	images = []
	for image in os.listdir(os.path.join(rootdir, f)):
		i = cv2.imread(os.path.join(rootdir, f, image))
		if i.shape[0] == 1080:
			crop = i[0:1080, 0:1080]
			images.append(crop)
	if len(images) != 0:
		im_v = cv2.hconcat(images) 
		cv2.imwrite('/home/ubuntu/Dance_data/rgb/balletmoco/concatballet/' + str(count) + '.jpg', im_v)
	count += 1
