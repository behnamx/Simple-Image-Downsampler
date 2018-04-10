import os
import cv2


high_res_directory = 'input/'
low_res_directory = 'output/'

# Downsample HR images
for filename in os.listdir(high_res_directory):

    # Read HR image
    high_res = cv2.imread(os.path.join(high_res_directory, filename))

    # Blur with Gaussian kernel of width sigma=1
    high_res = cv2.GaussianBlur(hr_img, (0, 0), 1, 1)


    # Downsample image 4x
    low_res_4x = cv2.resize(high_res, (0, 0), fx=0.25, fy=0.25,
                           interpolation=cv2.INTER_CUBIC)

    cv2.imwrite(os.path.join(low_res_directory, filename), low_res_4x)
