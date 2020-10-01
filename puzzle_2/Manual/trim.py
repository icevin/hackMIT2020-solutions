import os
from PIL import Image
import numpy as np
import json



if __name__ == "__main__":
    file1 = open('assignment.txt', 'r') 
    count = -1

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
            os.remove('images/' + str(count) + '.png')
            continue
        else:
            a = line.strip('()\n ')
            a = list(map(int, a.replace(' ', '').split(",")))
            a.append(count)
            # print(a)
            pixels.append(a)

    # print(pixels)   
    file1.close() 