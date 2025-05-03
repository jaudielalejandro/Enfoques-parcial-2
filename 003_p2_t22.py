from sklearn.ensemble import AdaBoostClassifier

modelo_boost = AdaBoostClassifier()
modelo_boost.fit(X_train, y_train)

print("Predicción Boosting:", modelo_boost.predict([X_test[0]]))
