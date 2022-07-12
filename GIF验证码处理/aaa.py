from PIL import Image
import numpy as np
import cv2

path = r"ccc.gif"
image =Image.open(path)

shapes = []
for i in range(1,4):
    image.seek(i)
    image.save(f'image/{i}.png')
    shapes.append(np.array(image))

result = np.subtract(shapes[0], shapes[2])
result2 = np.subtract(shapes[0], shapes[1])
result3 = np.subtract(shapes[1], shapes[2])
cv2.imwrite("image/result.png", shapes[0] + result+result2+result3)

