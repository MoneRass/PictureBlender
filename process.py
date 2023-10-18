import cv2
import numpy as np
import matplotlib.pyplot as plt

def blend(img1, img2):

    image1 = cv2.imread(img1)
    image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)

    image2 = cv2.imread(img2)
    image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)

    image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))

    all_pixel = image1.shape[1] * image1.shape[0]

    color = ('b','g','r')

    #Loop through each color sequentially
    for i,col in enumerate(color):
        
        #To use OpenCV's calcHist function, uncomment below
        histr = cv2.calcHist([image1],[i],None,[256],[0,256])
        
        #To use numpy histogram function, uncomment below
        #histr, _ = np.histogram(colorimage[:,:,i],256,[0,256])
        histr = [i/all_pixel for i in histr]

    image1_sum = []

    # plt.subplot(333)

    #Loop through each color sequentially
    for i,col in enumerate(color):
        
        #To use OpenCV's calcHist function, uncomment below
        histr = cv2.calcHist([image1],[i],None,[256],[0,256])
        
        s = 0
        cdf = []
        for i in histr:
            s += i
            image1_sum.append(int(s))
            cdf.append(s/all_pixel) 

    #Loop through each color sequentially
    for i,col in enumerate(color):
        
        #To use OpenCV's calcHist function, uncomment below
        histr = cv2.calcHist([image2],[i],None,[256],[0,256])
        
        #To use numpy histogram function, uncomment below
        #histr, _ = np.histogram(colorimage[:,:,i],256,[0,256])
        histr = [i/all_pixel for i in histr]
    
    image2_sum = []

    #Loop through each color sequentially
    for i,col in enumerate(color):
        
        #To use OpenCV's calcHist function, uncomment below
        histr = cv2.calcHist([image2],[i],None,[256],[0,256])
        
        #To use numpy histogram function, uncomment below
        #histr, _ = np.histogram(colorimage[:,:,i],256,[0,256])
        s = 0
        cdf = []
        for i in histr:
            s += i
            image2_sum.append(int(s))
            cdf.append(s/all_pixel) 
   
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
    image1_blue = image1[:,:,0].flatten()
    image2_blue = image2[:,:,0].flatten()
    for i in range(len(image1_blue)):
        image1_blue_cdf = image1_sum[image1_blue[i]]
        mapping = nearest_val(image1_blue_cdf, image2_sum[0:256])
        image1_blue[i] = mapping
    image1_blue = np.reshape(image1_blue,(image1.shape[0],image1.shape[1]))

    #green
    image1_green = image1[:,:,1].flatten()
    image2_green = image2[:,:,1].flatten()
    for i in range(len(image1_green)):
        image1_green_cdf = image1_sum[image1_green[i]+256]
        mapping = nearest_val(image1_green_cdf, image2_sum[256:512])
        image1_green[i] = mapping
    image1_green = np.reshape(image1_green,(image1.shape[0],image1.shape[1]))

    #red
    image1_red = image1[:,:,2].flatten()
    image2_red = image2[:,:,2].flatten()
    for i in range(len(image1_red)):
        image1_red_cdf = image1_sum[image1_red[i]+512]
        mapping = nearest_val(image1_red_cdf, image2_sum[512:768])
        image1_red[i] = mapping
    image1_red = np.reshape(image1_red,(image1.shape[0],image1.shape[1]))

    #res
    res = image1.copy()
    res[:,:,0] = image1_blue
    res[:,:,1] = image1_green
    res[:,:,2] = image1_red

    
   
    for i,col in enumerate(color):
        
        #To use OpenCV's calcHist function, uncomment below
        histr = cv2.calcHist([res],[i],None,[256],[0,256])
        
        #To use numpy histogram function, uncomment below
        #histr, _ = np.histogram(colorimage[:,:,i],256,[0,256])
        histr = [i/all_pixel for i in histr]
    #     plt.plot(histr, color=col)

    # plt.title("Result Image")

    image2_sum = []

    # plt.subplot(339)

    #Loop through each color sequentially
    for i,col in enumerate(color):
        
        #To use OpenCV's calcHist function, uncomment below
        histr = cv2.calcHist([res],[i],None,[256],[0,256])
        
        #To use numpy histogram function, uncomment below
        #histr, _ = np.histogram(colorimage[:,:,i],256,[0,256])
        s = 0
        cdf = []
        for i in histr:
            s += i
            cdf.append(s/all_pixel) 
    
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

#blend('img/doraemon.png','img/lav.jpg')