imagen = cv2.imread("imagen.jpg", cv2.IMREAD_GRAYSCALE)

# Filtro gaussiano para suavizar
imagen_suavizada = cv2.GaussianBlur(imagen, (5, 5), 0)

# Filtro de mediana
imagen_mediana = cv2.medianBlur(imagen, 5)
