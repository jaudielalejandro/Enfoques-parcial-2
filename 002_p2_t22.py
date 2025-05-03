from sklearn.tree import DecisionTreeRegressor

modelo_m5 = DecisionTreeRegressor()
modelo_m5.fit(X_train, y_train)

print("Predicción M5:", modelo_m5.predict([X_test[0]]))
