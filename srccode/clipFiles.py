import os
import random
import imageio
rootdir = '/home/ubuntu/Dance_data/rgb'

dance_categories = os.listdir(rootdir)
for dance in ["ballet"]:
#	if dance not in ["cha", "pasodoble", "tap", "jive", "rumba", "ballet", "break", "flamenco", "foxtrot", "latin", "quickstep", "square", "swing", "tango", "waltz"]:
		#continue
	## get list of video names
	video_names = [f[0:-8] for f in os.listdir(os.path.join(rootdir, dance))]
	video_names = list(set(video_names))
	for video in video_names:
		os.system("mkdir ./balletmoco/" + video)
		for i in range(1,33):
			numZeros = 4-len(str(i))
			zeros = "0"*numZeros
			os.system("cp " + os.path.join(rootdir, dance) + "/" + video + zeros + str(i) + ".jpg ./balletmoco/" + video + "/")


