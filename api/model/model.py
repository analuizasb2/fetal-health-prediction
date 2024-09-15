from pickle import load

class FetalHealthModel:
    def __init__(self):
        filename = '../pipelines/model_fetalhealth.pkl'
        self.model = load(open(filename, 'rb'))

    def classify_patient(self, input_data):
        return self.model.predict(input_data)