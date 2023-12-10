import numpy as np
from PIL import Image

img = np.array(Image.open('cat.jpg', 'r'))
img[:200, :, (0, 1)] = 0
img[200:400, :, (1, 2)] = 0
img[400:, :, (0, 2)] = 0
img1 = Image.fromarray(img)
img1.save('HW75.png', format='PNG')
