import os
import cv2


high_res_directory = 'input/'
low_res_directory = 'output/'

# Downsample High res images in output directory
for filename in os.listdir(high_res_directory):

    # Read high res images from input directory
    high_res = cv2.imread(os.path.join(high_res_directory, filename))

    # Blur images with gaussian
    high_res = cv2.GaussianBlur(high_res, (0, 0), 1, 1)


    # Resize 1/4
    low_res_4x = cv2.resize(high_res, (0, 0), fx=0.25, fy=0.25,
                           interpolation=cv2.INTER_CUBIC)

    cv2.imwrite(os.path.join(low_res_directory, filename), low_res_4x)
