# Conectividad de componentes
imagen_binaria = cv2.threshold(imagen, 127, 255, cv2.THRESH_BINARY)[1]
num_labels, etiquetas = cv2.connectedComponents(imagen_binaria)
print(f"Objetos encontrados: {num_labels - 1}")
