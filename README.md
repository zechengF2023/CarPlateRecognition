<p>data在Car-plate-location-1 folder中</p>
<p>训练好的weight在runs/train/yolov5s_results/weights/best.py</p>
<p>detect.py: 173-182行负责用pytesseract识别文字</p>
<p>plot.py: save_one_box function负责save and return cropped image</p>
<p>detect command example(在yolov5 directory下运行）：
<br>
python detect.py --weights ./runs/train/yolov5s_results/weights/best.pt --source /Users/guozechen/Documents/Car_plate_recognition/yolov5/Car-plate-location-1/test/images/Cars12_png.rf.9bf1aca93873b24d170b15e1329fa62f.jpg --save-crop</p>
