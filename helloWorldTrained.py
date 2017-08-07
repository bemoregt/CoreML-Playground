from sklearn.externals import joblib

classifier = joblib.load('myModel.pkl')

print classifier.predict([[150, 0]])
