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