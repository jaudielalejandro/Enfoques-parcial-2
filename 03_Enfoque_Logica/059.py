from sklearn.metrics import accuracy_score

pred1 = modelo_id3.predict(X_test)
pred2 = modelo_boost.predict(X_test)

acc1 = accuracy_score(y_test, pred1)
acc2 = accuracy_score(y_test, pred2)

print("ID3 Accuracy:", acc1)
print("Boosting Accuracy:", acc2)
