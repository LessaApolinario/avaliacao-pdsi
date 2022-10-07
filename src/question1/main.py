import numpy as np
import cv2 as cv


def getRedMask(image: cv.Mat) -> cv.Mat:
    lower_hsv_red0 = np.array([0, 175, 20])
    lower_hsv_red1 = np.array([170, 175, 20])

    upper_hsv_red0 = np.array([10, 255, 255])
    upper_hsv_red1 = np.array([180, 255, 255])

    mask_red_0 = cv.inRange(image, lower_hsv_red0, upper_hsv_red0)
    mask_red_1 = cv.inRange(image, lower_hsv_red1, upper_hsv_red1)
    mask: cv.Mat = mask_red_0 + mask_red_1
    return mask


def getGreenMask(image: cv.Mat) -> cv.Mat:
    lower_hsv_green = np.array([40, 150, 20])
    upper_hsv_green = np.array([70, 255, 255])

    mask = cv.inRange(image, lower_hsv_green, upper_hsv_green)
    return mask


def putTextOnRedPixels(image: cv.Mat) -> cv.Mat:
    for i, j in np.ndindex(image.shape[:-1]):
        pixel = image[i, j]
        if (pixel[0] >= 0 and pixel[0] <= 170) or (pixel[0] >= 10 and pixel[0] <= 180):
            cv.putText(
                img=image,
                text="vermelho",
                org=(i, j),
                fontFace=cv.FONT_HERSHEY_SIMPLEX,
                fontScale=1,
                color=(255, 255, 255),
                thickness=1,
                lineType=cv.LINE_AA
            )

    newImage = image.copy()
    return newImage


def putTextOnGreenPixels(image: cv.Mat):
    for i, j in np.ndindex(image.shape[:-1]):
        pixel = image[i, j]
        if pixel[0] >= 40 and pixel[0] <= 70:
            cv.putText(
                img=image,
                text="vermelho",
                org=(i, j),
                fontFace=cv.FONT_HERSHEY_SIMPLEX,
                fontScale=1,
                color=(255, 255, 255),
                thickness=1,
                lineType=cv.LINE_AA
            )

    newImage = image.copy()
    return newImage


def identifyColors() -> None:
    image = cv.imread("paisagem.jfif", cv.IMREAD_COLOR)

    if image is None:
        print("impossivel carregar a imagem!")
        return

    greenMask = getGreenMask(image=image)

    green = cv.bitwise_and(image, image, mask=greenMask)
    greenWarning = putTextOnGreenPixels(green)

    redMask = getRedMask(image=image)
    red = cv.bitwise_and(image, image, mask=redMask)

    redWarning = putTextOnRedPixels(red)

    cv.imshow("Imagem", image)
    cv.imshow("Green", greenWarning)
    cv.imshow("Red", redWarning)

    cv.waitKey(0)
    cv.destroyAllWindows()
