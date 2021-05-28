import cv2
import numpy as np


def resizeImages(image, size = 256):

    img = cv2.imread(image,cv2.IMREAD_UNCHANGED)
    interpolation = cv2.INTER_AREA
    height, width = img.shape[:2]

    c = None if len(img.shape) < 3 else img.shape[2]

    if height == width:
        return cv2.resize(img, (size, size), interpolation)

    if height > width:
        dif = height
    else:
        dif = width

    x_pos = int((dif - width) / 2.)
    y_pos = int((dif - height) / 2.)

    if c is None:
        mask = np.zeros((dif, dif), dtype=img.dtype)
        mask[y_pos:y_pos + height, x_pos:x_pos + width] = img[:height, :width]
    else:
        mask = np.zeros((dif, dif, c), dtype=img.dtype)
        mask[y_pos:y_pos + height, x_pos:x_pos + width, :] = img[:height, :width, :]

        output = cv2.resize(mask, (size, size), interpolation)
    print(output)
        # cv2.imwrite('D:/cv2-resize-image-50.jpeg', output)

    # return output

resizeImages("D:/cv2-resize-image-50.png")