import os
import random
import imageio
rootdir = '/home/ubuntu/Dance_data/rgb'

dance_categories = os.listdir(rootdir)
for dance in dance_categories:
	if dance not in ["cha", "pasodoble", "tap", "jive", "rumba", "ballet", "break", "flamenco", "foxtrot", "latin", "quickstep", "square", "swing", "tango", "waltz"]:
		continue
	train_files = {}
	test_files = {}

        ## get list of video names
	video_names = [f[0:-8] for f in os.listdir(os.path.join(rootdir, dance))]
	video_names = list(set(video_names))
	keep_names = []
	for i in video_names:
		frame_to_check = i + "0001.jpg"
		img = imageio.imread(os.path.join(rootdir, dance, frame_to_check))
		shape = img.shape
		
		if shape == (720, 1280, 3):
			keep_names.append(i)
#	print(len(keep_names))
	video_names = keep_names
	count = len(video_names)
	random.shuffle(video_names)
	test_number = int(count / 5)
	train_videos = video_names[:(count-test_number)]
	test_videos = video_names[count-test_number+1:]
#       print(len(train_videos))
#       print(len(test_videos))        
	for train in train_videos:
		os.system("mkdir ./train/" + train)
		os.system("cp ./" + dance + "/" + train + "* ./train/" + train + "/.")
	for test in test_videos:
		os.system("mkdir ./test/" + test)
		os.system("cp ./" + dance + "/" + test + "* ./test/" + test + "/.")
