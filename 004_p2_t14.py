# Filtro de Laplaciano para texturas
laplaciano = cv2.Laplacian(imagen, cv2.CV_64F)

# Filtro de Gabor (usando SciPy y OpenCV)
import cv2
def filtro_gabor(img):
    kernel = cv2.getGaborKernel((21, 21), 5.0, np.pi/4, 10.0, 0.5, 0)
    return cv2.filter2D(img, cv2.CV_8UC3, kernel)
