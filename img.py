import numpy as np
from PIL import Image

img = np.array(Image.open('cat.jpg', 'r'))
print(img[0, 0])

imgR = img.copy()
imgR[:,:,(1,2)] = 0
img1 = Image.fromarray(imgR)
img1.save('R.png', format='PNG')

imgG = img.copy()
imgG[:,:,(0,2)] = 0
img1 = Image.fromarray(imgG)
img1.save('G.png', format='PNG')

imgV = img.copy()
imgV[:,:,(1)] = 0
img1 = Image.fromarray(imgV)
img1.save('V.png', format='PNG')

imgGRAY = img.copy()
imgGRAY = np.mean(imgGRAY, axis=2).astype(np.uint8)
img1 = Image.fromarray(imgGRAY)
img1.save('GRAY.png', format='PNG')

imgGB = img.copy()
imgGB[:300,:400,(0,2)] = 0
imgGB[300:,400:,(0,1)] = 0
imgGB[:300,400:,(1,2)] = 0
gray = np.mean(imgGB[300:,:400,:], axis=2)
imgGB[300:,:400,0] = gray
imgGB[300:,:400,1] = gray
imgGB[300:,:400,2] = gray
img1 = Image.fromarray(imgGB)
img1.save('GB.png', format='PNG')