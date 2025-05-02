from sklearn import svm

# Datos
X = [[0, 0], [1, 1]]
y = [0, 1]

# SVM con núcleo RBF (gaussiano)
clf = svm.SVC(kernel='rbf')
clf.fit(X, y)

print(clf.predict([[0.5, 0.5]]))
