import os
import cv2
import numpy as np
rootdir = '/home/ubuntu/Dance_data/rgb/moco'
folders = os.listdir(rootdir)
for dance in folders:
	count = 0
	os.system('mkdir /home/ubuntu/Dance_data/rgb/moco/concat' + dance)
	for f in os.listdir(os.path.join(rootdir, dance)):
		images = []
		for image in os.listdir(os.path.join(rootdir, dance, f)):
			i = cv2.imread(os.path.join(rootdir, dance, f, image))
			if i.shape[0] == 1080:
				crop = i[0:1080, 0:1080]
				images.append(crop)
		if len(images) != 0:
			im_v = cv2.hconcat(images) 
			cv2.imwrite('/home/ubuntu/Dance_data/rgb/moco/concat' + dance + "/"  + str(count) + '.jpg', im_v)
		count += 1

