./darknet detector train configs/obj.data configs/yolo-obj.cfg configs/darknet53.conv.74 -mjpeg_port 8090
./darknet detector calc_anchors configs/obj.data -width 512 -height 256 -show