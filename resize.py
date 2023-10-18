import cv2
import numpy as np
from typing import Union
import matplotlib.pyplot as plt

def resize_and_save(input_fp: str, scale: Union[float, int]) -> np.ndarray:

    _scale = lambda dim, s: int(dim * s / 100)
    im: np.ndarray = cv2.imread(input_fp)
    height, width, channels = im.shape
    new_width: int = _scale(width, scale)
    new_height: int = _scale(height, scale)
    new_dim: tuple = (new_width, new_height)
    
    resized_image = cv2.resize(src=im, dsize=new_dim, interpolation=cv2.INTER_LINEAR)
    
    print(new_dim)
    resized_image = cv2.cvtColor(resized_image, cv2.COLOR_RGB2BGR)

    # Save the resized image
    save_resize(input_fp, resized_image)
    
    plt.imshow(resized_image)
    plt.show()
    
    return resized_image

def save_resize(img, resized_image):
    output_name = img.split('/')
    output_name = output_name[-1]
    output_folder = 'resized_img'
    output_path = output_folder + '/' + output_name
    cv2.imwrite(output_path, resized_image)

#resize_and_save('blended_img/blended_fuji_lav.jpg', 45)
