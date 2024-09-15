import joblib
from sklearn.tree import DecisionTreeClassifier

class FetalHealthClassifier:
    def __init__(self):
        filename = './pipelines/model_fetalhealth.pkl'
        self.model = joblib.load(open(filename, 'rb'))

    def classify_patient(self, input_data):
        return self.model.predict(input_data)