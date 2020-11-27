# HW2_Report
Code for digits dection
---Street View House Numbers
- [Data Preprocessing](#First)
- [Model](#Forth)
- [Train](#Fifth)
- [Speed Benchmark](#Sixth)
- [Submit](#Seventh)

<h2 id="First">Data Preprocessing</h2>

trasfer the data from .mat to HDF5
<pre><code>for index in range(33402):
    file = open("temp_train/"+str(index+1)+".txt","w")
    item = hdf5_data['digitStruct']['bbox'][index].item()
    for key in ['label', 'left', 'top', 'width', 'height']:
        attr = hdf5_data[item][key]
        values = [hdf5_data[attr[i].item()][0][0]
            for i in range(len(attr))] if len(attr) > 1 else [attr[0][0]]
        attrs[key] = values
    file.write(str(len(attrs['label'])))
    for j in range(len(attrs['label'])):
        file.write( "\n" + str(int(attrs['left'][j])) + " " + str(int(attrs['top'][j])) + " " + str(int(attrs['width'][j])) + " " + str(int(attrs['height'][j])) + " " + str(int(attrs['label'][j])) + " " )
</code></pre>

make the .txt of all train image
<pre><code>file = open("train.txt","w")
for i in range(len(imgs)):
    file.write('train/'+str(imgs[i])+'\n') 
file.close()
</code></pre>

process and covert data to yolo format
<pre><code>""" Process """
for txt_name in txt_name_list:
    
    """ Open input text files """
    txt_path = temp + txt_name
    print("Input:" + txt_path)
    txt_file = open(txt_path, "r")
    lines = txt_file.read().split('\n')
    
    """ Open output text files """
    txt_outpath = out + txt_name
    print("Output:" + txt_outpath)
    txt_outfile = open(txt_outpath, "w")
    
    
    """ Convert the data to YOLO format """
    ct = 0
    for line in lines:
        if(len(line) >= 2):
            ct = ct + 1
            print(line + "\n")
            elems = line.split(' ')
            print(elems)
            xmin = elems[0]
            xmax = elems[2]
            ymin = elems[1]
            ymax = elems[3]
            cls = elems[4]
            
            img_path = str('train/%s.png'%(os.path.splitext(txt_name)[0]))
            
            im=Image.open(img_path)
            w= int(im.size[0])
            h= int(im.size[1])
            
            print('W H = ', w, h)
            b = (float(xmin), float(xmax), float(ymin), float(ymax))
            print('B = ', b)
            bb = convert((w,h), b)
            print(bb)
            print("CLS = ", cls)
            txt_outfile.write(str(cls) + " " + " ".join([str(a) for a in bb]) + '\n')
</code></pre>


<h2 id="Forth">Model</h2>


I use Yolov3 darknet model

read the weight and cfg from darknet
<pre><code>net = cv2.dnn.readNetFromDarknet(configPath, weightsPath)</code></pre>
<h2 id="Fifth">Train</h2>

I trained YoloV3 from: https://github.com/AlexeyAB/darknet

I use the anchor values:  
29,67, 37,112, 57,112, 46,166, 64,150, 66,195, 85,166, 90,205, 121,204

The class in obj.names is from 0 to 10 (since number 0 = 10) not 1 to 10 because yolo was only able to train from index 0. So, the class would be 11 not 10.  

In this part, we used pretrained weight darknet53.conv.74 to get better result. For the model architecture, we used YoloV3.
<h2 id="Sixth">Speed Benchmark</h2> 

We tried to test the weight on Google Colab and we got the result 521 ms per loop.

<h2 id="Seventh">Submit</h2>

The dicts is all of my predict to the test image
<pre><code>with open('0616039.json', 'w') as fp:
        json.dump(dicts, fp)

</code></pre>