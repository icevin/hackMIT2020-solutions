from PIL import Image
import numpy as np

w, h = 690, 690
data = np.zeros((h, w, 3), dtype=np.uint8)
data[0:5, 0:5] = [255, 0, 0] # red patch in upper left
img = Image.fromarray(data, 'RGB')
img.save('out.png')
img.show()