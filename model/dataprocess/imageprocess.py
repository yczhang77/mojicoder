#!/usr/bin/env python
#this file is used to process image to rich the dataset..
import os
import sys
import shutil
import cv2
import numpy as np
import scipy.misc

#this function used to generate rotated img-npz file.
def generate_rotate_image_set(img_path, output_path, index, img_size = 128, output_size = 21):
    #save all output paths...
    paths = []
    indexstr = '0'
    if index < 10:
        indexstr += str(index)
    else:
        indexstr = str(index)
    for count in range(output_size):
        tmp_path = output_path + os.path.basename(img_path)\
        [:os.path.basename(img_path).find('.png')] + '_' + str(count) + '.png'
        paths.append(tmp_path)

    #set bkg color to white and rotate it following a loop.
    imgs = []
    img = cv2.imread(img_path, 0) #use grayscale
    #cv2.imshow('image',img)
    #cv2.waitKey(0)
    img = cv2.resize(img, (img_size, img_size))
    tmp = np.uint8(np.clip(1.2*img, 0, 255))
    for a in range(img_size):
        for b in range(img_size):
            if (a-63.5)*(a-63.5)+(b-63.5)*(b-63.5) >63.5*63.5 and img[a][b]== 0:
                tmp[a][b] = 255
    imgs.append(tmp)

    for rotate_times in range(round((output_size - 1)/2)):
        rotate_matrix = cv2.getRotationMatrix2D((img_size/2, img_size/2), 5*rotate_times, 1)
        anti_matrix = cv2.getRotationMatrix2D((img_size/2, img_size/2), -5*rotate_times, 1)
        result_img = cv2.warpAffine(tmp, rotate_matrix, (img_size, img_size), borderValue = (255, 255, 255))
        #cv2.imshow('image',result_img)
        #cv2.waitKey(0)
        anti_img = cv2.warpAffine(tmp, anti_matrix, (img_size, img_size), borderValue = (255, 255, 255))
        imgs.append(result_img)
        imgs.append(anti_img)

    for Path in range(len(paths)):
        scipy.misc.imsave(paths[Path], imgs[Path])
        #save_in(paths[Path])
        #npz_Path = paths[Path][: paths[Path].find('.png')]
        #img_npz(imgs[Path], npz_Path, mode = 0)

def save_in(path):
    newimg = cv2.imread(path, 0)
    print(path, newimg)
    cv2.imshow('image',newimg)
    cv2.waitKey(0)
    scipy.misc.imsave(path, newimg)

def img_npz(nparr, output_path, mode = 1):
    # mode 0：multiple files into array.
    # mode 1: single file convertion.
    directory = os.path.dirname(output_path)
    if mode == 1:
        for traverse in range(len(nparr)):
            print('hello')
    else:
        file_name = output_path
        np.savez_compressed('{}/{}'.format(directory, file_name), features = nparr)
        retrieve = np.load('{}/{}.npz'.format(directory, file_name))

        assert np.array_equal(nparr, retrieve)



if __name__ == '__main__':
    argv = sys.argv[1:]
    input_path = argv[0]
    output_path = '../../dataset/imgs/'
    if len(argv) >= 2:
        output_path = argv[1] + '\\'
    count = 0
    for file in os.listdir(input_path):
        if file.find('.png') != -1:
            img_path = '{}/{}'.format(input_path, file)
            generate_rotate_image_set(img_path, output_path, count)
            count += 1
