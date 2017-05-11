# -*- coding: utf-8 -*-
"""
Created on Wed May 10 10:12:49 2017

@author: tsrivas
"""

import cv2
import argparse
from color import color_transfer
import imutils
import numpy as np
# create an argument parser for reading the source and target images
ap=argparse.ArgumentParser()
ap.add_argument("-s","--source",help='Path to the source image')
ap.add_argument("-t","--target",help='Path to the target image')

args=vars(ap.parse_args())

# load the source and target images from disk
source=cv2.imread(args["source"])
target=cv2.imread(args["target"])

source=imutils.resize(source,height=400)
target=imutils.resize(target,height=400)
# Display the source and target images
#cv2.imshow("Source Image",source)
#cv2.imshow("Target Image",target)

# Apply the color transfer function to obtain the transferred iamge
transfer = color_transfer(source,target)
image=np.hstack( (source,target,transfer) )
# Display the transfer function
cv2.imshow("Transferred Image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()


