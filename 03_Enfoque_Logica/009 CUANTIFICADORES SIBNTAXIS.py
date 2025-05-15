from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y)

modelo_id3 = DecisionTreeClassifier(criterion="entropy")
modelo_id3.fit(X_train, y_train)

print("Predicción ID3:", modelo_id3.predict([X_test[0]]))
