import os
from PIL import Image
import numpy as np
import json
# make a prediction for a new image.
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import keras.backend as K
 
# load and prepare the image
def load_image(filename):
    # load the image
    img = load_img(filename, target_size=(32, 32))
    # convert to array
    img = img_to_array(img)
    # reshape into a single sample with 3 channels
    img = img.reshape(1, 32, 32, 3)
    # center pixel data
    img = img.astype('float32')
    img = img - [123.68, 116.779, 103.939]
    return img
 
model = load_model('small_model.h5')

# load an image and predict the class
def run_example(file):
    # load the image
    global model
    img = load_image(file)
    # load model
    # predict the class
    result = model.predict(img)
    return(result[0])

 
if __name__ == "__main__":
    file1 = open('assignment.txt', 'r') 
    count = 0

    pixels = []

    while True: 
        count += 1
    
        # Get next line from file 
        line = file1.readline() 
    
        # if line is empty 
        # end of file is reached 
        if not line: 
            break
        # print("Line{}: {}".format(count, line.strip())) 
        if line == '  \n': # empty
            continue
        else:
            a = line.strip('()\n ')
            a = list(map(int, a.replace(' ', '').split(",")))
            a.append(count)
            # print(a)
            pixels.append(a)

    # print(pixels)   
    file1.close() 

    w, h = 69, 69
    data = np.zeros((h, w, 3), dtype=np.uint8)

    c = 0

    for pixel in pixels:
        c += 1
        if c % 1000 == 0:
            img = Image.fromarray(data, 'RGB')
            img.save('out.png')
        # = (pixel[2], pixel[2], pixel[2])
         #print("({},{}){}".format(pixel[0], pixel[1], pixel[2]))
        file = 'images/' + str(pixel[2] - 1) + '.png'
        res = run_example(file)
        K.clear_session()
        if res > 0.5:
            data[pixel[0] - 1][pixel[1] - 1] = (255, 255, 255)
            print("1")
        else:
            data[pixel[0] - 1][pixel[1] - 1] = (0, 0, 0)
            print("0")


    #print(data[1][1])


    img = Image.fromarray(data.reshape((69,69)).astype('uint8')*255)
    img.save('out.png')
