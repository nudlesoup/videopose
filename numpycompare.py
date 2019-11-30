import numpy as np
a = np.load('/home/nudlesoup/Downloads/Set64_25fps.mp4.npz',allow_pickle=True)
b = np.load('/home/nudlesoup/Research/ProcessedDataset/Input/Set64_25fps.mp4.npz',allow_pickle=True)

# print(a.files)
# print(b.files)
print(a['keypoints'])
#print(b['keypoints'])