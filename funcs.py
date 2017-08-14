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
    def __init__(self,z_img=None,z_path=None):
        self.z_buf = z_img;
        self.z_path = z_path;


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
        #return None;
    
    
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
            
            
    

    


