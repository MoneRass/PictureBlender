
import cv2
import numpy as np
import matplotlib.pyplot as plt

def blend(img1, img2):

    base_img = cv2.imread(img1)
    color_img = cv2.imread(img2)

    base_img = cv2.cvtColor(base_img, cv2.COLOR_BGR2RGB)
    color_img = cv2.cvtColor(color_img, cv2.COLOR_BGR2RGB) 
    color_img = cv2.resize(color_img, (base_img.shape[1], base_img.shape[0]))


    color = ('b','g','r')
    base_img_sum = []

    #Loop through each color sequentially
    for i in range(len(color)):
        histr = cv2.calcHist([base_img],[i],None,[256],[0,256])
        s = 0
        for i in histr:
            s += i
            base_img_sum.append(int(s))

    color_img_sum = []

    #Loop through each color sequentially
    for i in range(len(color)):
        histr = cv2.calcHist([color_img],[i],None,[256],[0,256])
        s = 0
        for i in histr:
            s += i
            color_img_sum.append(int(s))
   
    def nearest_val(val,tarr):
        thres = 10e10
        dum_dex = 0
        for i in range(len(tarr)):
            dum_thres = abs(val-tarr[i]) 
            if dum_thres == 0:
                return i
            elif thres >= dum_thres:
                thres = dum_thres
                dum_dex = i
        return dum_dex

    #blue
    base_img_blue = base_img[:,:,0].flatten()
    for i in range(len(base_img_blue)):
        base_img_blue_cdf = base_img_sum[base_img_blue[i]]
        mapping = nearest_val(base_img_blue_cdf, color_img_sum[0:256])
        base_img_blue[i] = mapping
    base_img_blue = np.reshape(base_img_blue,(base_img.shape[0],base_img.shape[1]))

    #green
    base_img_green = base_img[:,:,1].flatten()
    for i in range(len(base_img_green)):
        base_img_green_cdf = base_img_sum[base_img_green[i]+256]
        mapping = nearest_val(base_img_green_cdf, color_img_sum[256:512])
        base_img_green[i] = mapping
    base_img_green = np.reshape(base_img_green,(base_img.shape[0],base_img.shape[1]))
    

    #red
    base_img_red = base_img[:,:,2].flatten()
    for i in range(len(base_img_red)):
        base_img_red_cdf = base_img_sum[base_img_red[i]+512]
        mapping = nearest_val(base_img_red_cdf, color_img_sum[512:768])
        base_img_red[i] = mapping
    base_img_red = np.reshape(base_img_red,(base_img.shape[0],base_img.shape[1]))

    #result
    res = base_img.copy()
    res[:,:,0] = base_img_blue
    res[:,:,1] = base_img_green
    res[:,:,2] = base_img_red

     # Save the resized image
    save_blend(img1, img2, res)

    plt.imshow(res)
    plt.show()


    return res

def save_blend(img1, img2, res):
    output_name1 = img1.split('/')
    output_name2 = img2.split('/')
    output_name = 'blended_'+output_name1[-1][:-4]+"_"+output_name2[-1]
    output_folder = 'blended_img'
    output_path = output_folder + '/' + output_name
    res = cv2.cvtColor(res, cv2.COLOR_RGB2BGR)
    cv2.imwrite(output_path, res)

# blend('img/doraemon.png','img/lav.jpg')