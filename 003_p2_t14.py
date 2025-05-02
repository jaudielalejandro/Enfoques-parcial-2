# Detección de bordes con Canny
bordes = cv2.Canny(imagen, 100, 200)

# Segmentación simple con umbral
_, binaria = cv2.threshold(imagen, 127, 255, cv2.THRESH_BINARY)
