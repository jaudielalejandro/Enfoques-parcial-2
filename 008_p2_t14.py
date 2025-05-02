cap = cv2.VideoCapture("video.mp4")
_, frame1 = cap.read()
_, frame2 = cap.read()

while cap.isOpened():
    dif = cv2.absdiff(frame1, frame2)
    gris = cv2.cvtColor(dif, cv2.COLOR_BGR2GRAY)
    _, binaria = cv2.threshold(gris, 25, 255, cv2.THRESH_BINARY)
    
    cv2.imshow("Movimiento", binaria)
    frame1 = frame2
    ret, frame2 = cap.read()
    if not ret or cv2.waitKey(30) == 27:
        break

cap.release()
cv2.destroyAllWindows()
