'''
Created on Jul 11, 2021

@author: nicomp
'''
from PIL import Image, ImageFilter, ImageDraw, ImageFont
import os, sys
import requests
from io import BytesIO


'''
    Load an image file from disk
    :param filename: The file to load
    :return the image object
'''
def load_image( filename ) :
    try:
        myimage = Image.open(filename)
        myimage.load()
        return myimage
    except:
        return None


def save_image( imageObject, outfilename ) :
    '''
    Save an image to disk
    :param imageObject: The Image to save
    :param outfilename: The target file
    '''
    imageObject.save( outfilename )

def blur_image(imageObject):
    # Doesn't look too different but it does blur a little. Depends on the original image
    blurred = imageObject.filter(ImageFilter.BLUR)
    # blurred = imageObject.filter(ImageFilter.EMBOSS)    # This produces dramatic results. 
    # blurred = imageObject.filter(ImageFilter.DETAIL)    # Doesn't look much different 
    return blurred


