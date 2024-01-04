# Face Detection using OpenCV and face_recognition

This repository contains a Python script to detect faces in an image using OpenCV and the `face_recognition` library.

## Requirements

- Python 3.x
- OpenCV (`cv2`)
- face_recognition

Install the required libraries using:

pip install opencv-python
pip install face_recognition

The script will read the image, perform face detection using two different models (HOG and CNN), and display the number of faces found in the image using each model.

## Description
The Python script face_detection.py performs face detection using two models:

HOG (Histogram of Oriented Gradients) & CNN (Convolutional Neural Network)
It reads an image, detects faces using both models, and prints the number of faces found using each model. Additionally, it displays the location of each detected face in the image.

Example
The script reads an image (1.jpg in this example) and displays it for testing purposes. Then it detects faces using HOG and CNN models, printing the number of faces found and their respective locations in the image.
