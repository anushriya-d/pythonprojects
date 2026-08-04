import imageio.v3 as iio 
from PIL import Image
import numpy as np


filenames = ['team-pic1.png', 'team-pic2.png']
images = [ ]

for filename in filenames:
    img = Image.open(filename).convert('RGB')   # force RGB
    images.append(np.array(img))

iio.imwrite('team.gif', images, duration = 500, loop = 0)
