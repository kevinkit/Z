# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 09:16:37 2017

@author: kevinkit
"""
import numpy as np




class Z:
    """    
        Class for Z-images augmentation
    """
    def __init__(self,z_img=None,z_rgb=None,z_path=None,z_hsv=None):
        self.z_buf = z_img
        self.z_rgb = z_rgb
        self.z_path = z_path
        self.z_hsv = z_hsv
        

    def anyRead(self,path=None):
        """
        Function reads out image and sets
        the z_buf member
        
        @param path Path to image. If not set, it will try to read the path 
        given to the construct
        @return returns True on success, false on fail. 
                
        """
        if path is None:
            path = self.z_path;
        
        try:
            from PIL import Image
            i = Image.open(path)
            self.z_buf = np.asarray(i)
        except Exception as e:
            print(e)
            
        try:
            import cv2
            i = cv2.imread(path)
            self.z_buf = np.asarray(i)
        except Exception as e:
            print(e)
            
        try:
            from scipy import misc
            i = misc.imread(path)
            self.z_buf = np.asarray(i)
        except Exception as e:
            print(e)
            
        
        if self.z_buf is None:
            print("No library found for reading images or image not found!");
            return False;
        else:
            return True;
        
        
    def depth2gray(self,img=None,weights=[1,1,1]):
        """
        Converts a one-sliced iamge to a three-sliced rgb image, by simply 
        copying the one slice to all slices    
        @param img If img is not specified, it will try to load it from the 
        member variable z_buf 
        @param weights a 3element list, where each element stays for a 
        multiplaction factor of each slice            
        
        """
        if img is None:
            img = self.z_buf;
        
        
        grey_mirror = [weights[0]*img,weights[1]*img,weights[2]*img];
        grey_mirror = np.transpose(grey_mirror,axes=(1,2,0))
        self.z_rgb =  grey_mirror;
        
    def hack2hsv(self,z_rgb=None):
        """
        Converts a three-sliced rgb z-buffer image to its hsv representation. 
        The desired input image can beachieved with the function depth2gray
        
        @param z_rgb three sliced valid z buffer image. If it is not provided, 
        the function will try to read it from a member variable
        
        """
        from skimage import color     
        if z_rgb is None:
            z_rgb = self.z_rgb
        
        z_rgb = np.asarray(z_rgb,dtype=np.uint16)
        
        hsv_d = color.rgb2hsv(z_rgb)
        hsv_d[:,:,0]  = hsv_d[:,:,2]
        hsv_d[:,:,1] = 0.3
        #Image.fromarray(np.asarray(255*hsv_d,dtype=np.uint8))
        self.z_hsv = color.hsv2rgb(hsv_d)
        #self.z_hsv = hsv_d;
        
    
    def showZImg(self,img=None):
        """
        Will show the image in the console for debugging purposes.
        If PIL cannot show the Image it will decrease the bit resolution
        to 8 Bit. Sometimes this function is not shown properly. 
        @param img Z-Buffer image, if it is not set it will try to read the 
        image either set by the constructor or by anyRead function
        
        
        
        """
        if img is None:
            img = self.z_buf;
    
        from PIL import Image
        
        try:
            Image.fromarray(img)
        except Exception as e :
            print(e)
            try:
                Image.fromarray(np.asarray(img/255,dtype=np.uint8))
                print("Decreased bit resolution to 8 bit for showing image")
            except Exception as e:
                print(e)
            
        
            
    
    
