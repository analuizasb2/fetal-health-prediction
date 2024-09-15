from pickle import load

class PreProcessor:
    def __init__(self):
        filename = '../pipelines/standardscaler_fetalhealth.pkl'
        self.scaler = load(open(filename, 'rb'))

    def pre_process(self, input_data):
        return self.scaler.transform(input_data)