from coremltools.converters import sklearn
from sklearn.externals import joblib

classifier = joblib.load('myModel.pkl')
coreml_model = sklearn.convert(classifier, ["weight", "skin"], "fruit")
coreml_model.author = "Ojete calor"

coreml_model.save('FruitsClassifier.mlmodel')
