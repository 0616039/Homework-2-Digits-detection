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


<h2 id="Forth">Model</h2>


I use Yolov3 model
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