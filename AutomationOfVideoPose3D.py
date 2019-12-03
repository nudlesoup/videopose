import os
import subprocess
for root, dirs, files in os.walk("/content/videos/VideoSizeAcc/"):
    for f in files:
        fullpath = os.path.join(root, f)
        filename=str(f)
        middlename=filename.split('.')[0]
        final_numpy=middlename+"finalnumpy"
        output=middlename+"RD.mp4"
        subprocess.run(["python","run.py","-d","custom","-k","myvideos","-arc","3,3,3,3,3","-c","checkpoint","--evaluate","pretrained_h36m_detectron_coco.bin","--render","--viz-subject",filename,"--viz-action","custom","--viz-camera","0","--viz-video",str(fullpath),"--viz-output",output,"--viz-export", final_numpy ])