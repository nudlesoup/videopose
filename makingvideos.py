# import os
#
# for root, dirs, files in os.walk("/home/nudlesoup/Research/datasets/Real_Dataset/Frames/Side/"):
#     for directory in dirs:
#         if(str(directory).find("Set")=="false"):
#              print(directory)
#

import os
import subprocess
path = r'/home/nudlesoup/Research/datasets/Real_Dataset/Frames/Temp/'

for (path, dirs, files) in os.walk(path):
    if(str(path).find("Side_0")!=-1):
        print ("Path:", path)
        name=str(path)
        subst=name[58:64]

        os.chdir(path)
        videoname='/home/nudlesoup/Research/datasets/Real_Dataset/{}_25fps.mp4'.format(subst)
        subprocess.call(['ffmpeg','-r','25','-s','1920x1080','-f','image2','-i','%06d.jpg','-codec:v','libx264','-crf','15','-pix_fmt','yuv420p',videoname])
    # print ("\nDirs:")
    # for d in dirs:
    #     print ('\t'+d)

    # print ("\nFiles:")
    # for f in files:
    #     print ('\t'+f)


