def hebb(X, y):
    W = np.dot(X.T, y)  # Hebb: W = x*yᵗ
    return W
