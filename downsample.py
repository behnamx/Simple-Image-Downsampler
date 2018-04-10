import os
import cv2


high_res_directory = 'input/'
low_res_directory = 'output/'

# Downsample HR images
for filename in os.listdir(hr_image_dir):

    # Read HR image
    hr_img = cv2.imread(os.path.join(hr_image_dir, filename))
    hr_img_dims = (hr_img.shape[1], hr_img.shape[0])

    # Blur with Gaussian kernel of width sigma=1
    hr_img = cv2.GaussianBlur(hr_img, (0, 0), 1, 1)


    # Downsample image 4x
    lr_img_4x = cv2.resize(hr_img, (0, 0), fx=0.25, fy=0.25,
                           interpolation=cv2.INTER_CUBIC)

    cv2.imwrite(os.path.join(lr_image_dir, filename), lr_img_4x)
