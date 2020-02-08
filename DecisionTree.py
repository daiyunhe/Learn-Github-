form sklearn import tree
y = [0, 0, 2] # 花类别
clf = tree.DecisionTreeClassifier(criterion = "entropy")

# After being fitted, the model can then be used to predict the class of samples:
print(clf.predict([[2., 2., 3., 4.],[2., 2., 3., 4.]]))
print(clf.predict([2,2,2,2])
      
