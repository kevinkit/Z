# Z
This repository offers some python (and mayber later matlab, c++ and so on) for working with depth images


## Dependencies

The project depends on:

- numpy
- scipy
- Pillow or OpenCV

## Fast Introduction

1. Create a z-Class object

```python
Z_obj = Z()
```

2. Specify the path to the file

```python
Z_obj.anyread('myfile.png')
```

Now the object holds the image in z_buf. However, you can do more things now, like converting the z buf grayscale image to a wavelength image, simply by doing the following: 


3. Convert depth image to gray scale image

```python
Z_obj.depth2gray()
```

4. Convert depth image to gray scale image

```python
Z_obj.hack2hsv()
```
