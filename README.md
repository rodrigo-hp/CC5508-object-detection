# CC5508-object-detection
Object detection in images using simple algorithms like manipulating color channels of an image, application of a threshold for obtaining binary images, searching for connected components inside an image using a Depth First Search algorithm and Disjoint Union Sets data structure, border extraction of connected components using a digital topology algorithm called "Moore Neighbour Contour Tracing Algorithm" and detection of circumferential figures.
The objective is to detect round yellow objects, specifically.

## Used tools
This project was built using Python 3.6, Anaconda 3, Spyder, OpenCV and Numpy.

## Run example
To detect objects in an image, run the next code:
```
python tarea1.py "IMAGE_PATH"
```
For example, detecting round yellow objects in the next image:
![alt text](https://github.com/rodrigo-hp/CC5508-object-detection/blob/master/im1.jpg)

Result:
![alt text](https://github.com/rodrigo-hp/CC5508-object-detection/blob/master/im1-output.jpg)
