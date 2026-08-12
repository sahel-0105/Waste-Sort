# WASTE SORT

This project is an AI-powered waste classification system that identifies different types of waste in real time using a camera.

The system displays the waste type, prediction confidence, and disposal instructions. It runs on an NVIDIA Jetson Orin Nano and provides a web interface for viewing the results in real time.

![add image descrition here](direct image link here)

## The Algorithm

This project uses ResNet18, a convolutional neural network (CNN), for image classification.

The camera captures an image of an object and sends it to the trained ResNet18 model. The model analyzes the image and predicts which waste category it belongs to. It also calculates a confidence score for the prediction.

The system classifies six types of waste:

1. Glass Waste
2. Metal Waste
3. Organic Waste
4. Paper & Cardboard Waste
5. Plastic Waste
6. Textile & Rubber Waste

After the waste is classified, the system displays the predicted waste type, confidence score, and corresponding disposal instructions.

How the Code Works
The project uses several Python programs for different parts of the system.

split-dataset.py
Splits the downloaded dataset into training, validation, and test sets before model training.
train.py
Runs inside a Docker container and is used to retrain the ResNet18 model using the prepared dataset.
my_imagenet.py
Runs the trained image classification model and adds disposal instructions to the classification results. It displays the predicted waste type and confidence score along with the corresponding disposal information.
run_waste.py
Provides the real-time web interface. It allows the camera feed and classification results to be viewed through a web browser.
The trained model is converted to ONNX format and used for inference on the NVIDIA Jetson Orin Nano.

## Running this project

1. Download the Dataset
Download the "Recyclable and Household Waste Classification" dataset from Kaggle.

Unzip the downloaded dataset.

2. Prepare the Dataset
Use split-dataset.py to divide the dataset into three subsets: Train, Val, Test

3. Retrain the Model
Enter the Docker container and use train.py to retrain the ResNet18 model using the prepared dataset.

After training, prepare the trained model in ONNX format for use on the NVIDIA Jetson Orin Nano.

4. Run the Classification System
Make sure the trained model and labels file are in the correct directories.

Run: python3 run_waste.py

5. Open the Web Interface
Open the following address in a web browser:

http://<Jetson-IP-address>:8554

The camera feed, waste classification, confidence score, and disposal instructions will be displayed in real time.

## Project Demo
![IMG_0226](https://github.com/user-attachments/assets/18b64042-65c6-45ee-9739-3ab301bc3cf2)
![IMG_0225](https://github.com/user-attachments/assets/36425981-97a2-4f4c-bffd-8f765a540823)

[View a video explanation here](video link)
