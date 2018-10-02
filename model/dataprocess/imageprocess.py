#!/usr/bin/env python

#this file is used to process image to rich the dataset..
import os
import sys
import shutil
import cv2
import numpy as np

#this function used to generate rotated img-npz file.
def generate_rotate_image_set(img_path, img_size = 64, output_size = 21):

    #set bkg color to white and rotate it following a loop.
    img = cv2.imread(img_path, 0) #use grayscale
    img = cv2.resize(img, (img_size, img_size))
    img = img.astype('uint8')
    tmp = np.uint8(np.clip(1.5*img+10, 0, 255))
    temp = np.hstack((img, tmp))
    for rotate_times in range(round((output_size - 1)/2)):
        rotate_matrix = cv2.getRotationMatrix2D((img_size/2, img_size/2), 5*rotate_times, 1)
        anti_matrix = cv2.getRotationMatrix2D((img_size/2, img_size/2), -5*rotate_times, 1)
        result_img = cv2.warpAffine(tmp, rotate_matrix, (img_size, img_size), borderValue = (255))
        anti_img = cv2.warpAffine(tmp, anti_matrix, (img_size, img_size), borderValue = (255))
        processed_pair = np.hstack((result_img, anti_img))
        temp = np.vstack((temp, processed_pair))
    cv2.imshow('image', temp)
    cv2.waitKey(0)

if __name__ =='__main__':
    argv = sys.argv[1:]
    generate_rotate_image_set(argv[0])
