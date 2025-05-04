# Detección de rostros con Haar Cascade
detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
imagen = cv2.imread("rostro.jpg")
grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

caras = detector.detectMultiScale(grises)
for (x, y, w, h) in caras:
    cv2.rectangle(imagen, (x, y), (x+w, y+h), (255, 0, 0), 2)
