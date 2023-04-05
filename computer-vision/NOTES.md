# Finding Lane Lines
## 2.- Grayscale Conversion
### Edge Detection
Identify sharp changes in intensity in adjacent pixels
![edge_detection](/computer-vision/static/MD/edge_detection.png)
An image can be read as a matrix, an array of pixels.
A pixel contains the light intensity at some location at the image.

Each pixel intensity denoted by a numeric value that ranges from 0 to 255.
An intensity of 0 means no intensity, completely black,
255 means the highest intensity, completely white.
![pixel_intensity](/computer-vision/static/MD/pixel_intensity.png)

<br>

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

---
## 3.- Gaussian Blur (Reduce Noise and smooth the image)
![image](/computer-vision/static/MD/gaussian-example.png)
![image](/computer-vision/static/MD/grayscale-image-pixels.png)
averaging out the pixels in the image to reduce noise, will be done with a kernel.
This kernel essentially of a normally distributed numbers is run accross the entire image and sets each pixel value equal to the weighted average of its neighboring pixels, smoothering the image.
![image](/computer-vision/static/MD/kernel.png)

Example:
![image](/computer-vision/static/MD/gaussian-kernel.png)
5x5 kernel, the size depends on specif situation, but 5x5 is a good size for most cases.
It will return a new image with the gaussian blur by convolving the image with a kernel of Gaussian values, reduces noise in the image
![image](/computer-vision/static/MD/gaussian-kernel-02.png)

---

## 4.- Canny
Canny method to identify edges in the image.
Recall that an edge corresponds to a region in an image where there is a sharp change in intensity or in color between adjacent pixels.

The change in brightness over a series of pixels is the **Gradient**.
Strong gradient indicates a steep change, where a small gradient a shallow change. 
![image](/computer-vision/static/MD/gradient-change.png)

<br>

Must represent the image in a 2-dimensional coordinates space, **x** and **y**
![image](/computer-vision/static/MD/x%20and%20y%20in%20gradient.png)

### f(x, y)
___What operator can we use to determine rapid changes in brightness in the image?___
<br>
**Candy Function**
<br>
It will perform a derivative on our function in both x and y directions.
Measuring the change intensity with respect to adjacent pixels. <br>
A small derivative is a small change in intensity, where a big derivative is a big change. <br>

By computing the derivative in all directions of the image, we're computing the gradients.

![image](/computer-vision/static/MD/canny_function_example.png)