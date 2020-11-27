import os

imgs = []
for img in os.listdir('train'):
    if img.endswith('.png'):
        imgs.append(img)
        
imgs = sorted(imgs,key=lambda x: int(os.path.splitext(x)[0]))

file = open("train.txt","w")
for i in range(len(imgs)):
    file.write('train/'+str(imgs[i])+'\n') 
file.close()