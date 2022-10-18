import cv2
import os
import pathlib

SOURCEFOLDER    = '012_video_sources'
DEST            = '011_img_sources'
VIDEO           = 'junction_traffic_gray'

vidcap = cv2.VideoCapture(SOURCEFOLDER+f'/{VIDEO}.mp4')
success,image = vidcap.read()
count = 0

path = pathlib.Path(DEST+'/'+VIDEO+'/')
path.mkdir(parents=True, exist_ok=True)

print(f'Start reading frames from: {VIDEO}.mp4')
while success:
  cv2.imwrite(DEST+'/'+VIDEO+'/'+f"frame_{count}.jpg", image)     # save frame as JPEG file      
  success,image = vidcap.read()
  
  count += 1
print(f'Finished & saved to {path}')
