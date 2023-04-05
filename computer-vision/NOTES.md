# 2.- Finding Lane Lines
## Grayscale Conversion
### Edge Detection
Identify sharp changes in intensity in adjacent pixels
![edge_detection](/computer-vision/static/MD/edge_detection.png)
An image can be read as a matrix, an array of pixels.
A pixel contains the light intensity at some location at the image.

Each pixel intensity denoted by a numeric value that ranges from 0 to 255.
An intensity of 0 means no intensity, completely black,
255 means the highest intensity, completely white.
![pixel_intensity](/computer-vision/static/MD/pixel_intensity.png)

---

### Gradient
Measure of change in brightness over adjacent pixels
Strong gradient => steep change
Small gradient => shallow change
![image](/computer-vision/static/MD/gradient.png)

<br>

An edge is defined by the difference in intensity values in adjacent pixels 
![image](/computer-vision/static/MD/original-to-gradient.png)
wherever there's a sharp change in intensity, a rapid change in brightness, wherever there's a strong gradient, there is a corresponding bright pixel in the gradient image, by tracing out all of these pixels we obtain the edges.

---

### Example of a multi-step process
#### Step 1 - Convert the image to Gray Scale
![image](/computer-vision/static/test_lane_02.png)
![image](/computer-vision/static/MD/original-to-gray-scale.png)

**Why to grayscale?**
Images are made up of pixels, a 3-channel color image of (RGB), 3 intensity values, whereas a grayscale image only has one channel, each pixel with only one intensity value, ranging from 0 to 255.

**Using a grayscale image processing a single channel is faster than processing a 3-channel color image and less computational intensive**