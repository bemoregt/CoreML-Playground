from sklearn import tree

# Bumpy: 0
# Smooth: 1
features = [[140, 1], [130, 1], [150, 0], [170, 0]]

# Apple: 0
# Orange: 1
labels = [0, 0, 1, 1]

classifier = tree.DecisionTreeClassifier()
classifier = classifier.fit(features, labels)

from sklearn.externals import joblib
joblib.dump(classifier, 'myModel.pkl')
