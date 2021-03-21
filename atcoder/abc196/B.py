# B
X = input()
i = X.find('.')
if i > -1:
    print(X[:i])
else:
    print(X)