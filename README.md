## image-recognition
# Swamphacks 2020 - Sage
January 31 - February 2, 2020

Authors: Song Li (Gnoseil), Evan Rupert (evanrupert), Varun Puri (vmpuri), Stephen Lantin (slantin)

A company leader losing track of half of his workforce in the office. A software engineer whose boss might as well be a mirage. A graduate student knocking on the door of his advisor's office, only to hear nothing in return, and an intern losing his supervisor on the manufacturing floor. The inspiration for Sage arose from a frustration so small as to be nagging, yet so ubiquitous among our team members--where are our coworkers?

Sage uses facial recognition to identify people entering and leaving a building or room. It does this by first storing images of an employee on a Google Cloud Storage bucket (i.e., during a company's onboarding process). Then, as a person passes through a doorway, a camera takes an image of them, and classifies the image by name. A name, image, and timestamp are displayed on a web application hosted within a Compute Engine VM instance in the Google Cloud Platform.

Sage consists of three parts:

<b>1) Model training with OpenCV</b>
We trained a machine learning model with a facial dataset available in Python's OpenCV. Training was done using a Haar classifier cascade<sup>1</sup>, as it is more computationally efficient than detecting features by means of pixel intensity only<sup>2</sup>.

<b>2) Image Capture</b>
Images of the "onboarding process" were captured using an standard laptop webcam. When an employee walks through a doorway, a camera takes an image of them.

<b>3) Web Application</b>
The back-end of the web application was written in node.js with Express. It used web sockets to connect components for real-time communication. We used the front-end framework vue.js to make a clean, fun dashboard to present information to employees.

See https://devpost.com/software/sage-kpmcgw for more information.

<sup>1</sup>Paul Viola and Michael J. Jones. Rapid Object Detection using a Boosted Cascade of Simple Features. IEEE CVPR, 2001

<sup>2</sup>Papageorgiou, Oren and Poggio, "A general framework for object detection", International Conference on Computer Vision, 1998.
