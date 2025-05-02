import cv2
import numpy as np

# Crear una imagen negra y dibujar un círculo
imagen = np.zeros((300, 300, 3), dtype=np.uint8)
cv2.circle(imagen, (150, 150), 50, (0, 255, 0), -1)

cv2.imwrite("circulo.png", imagen)
