import pytesseract
import cv2

imagen = cv2.imread("texto.jpg")
texto = pytesseract.image_to_string(imagen, lang='spa')
print(texto)
