import subprocess
subprocess.run(["python3","my_imagenet.py", "--model=models/waste3/resnet18.onnx", "--input_blob=input_0", "--output_blob=output_0", "--labels=models/waste3/labels.txt",
 "/dev/video0", "webrtc://@:8554/output"])


#--topK=2