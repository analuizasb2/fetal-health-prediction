import numpy as np
import pickle
from schema.cardiotocogram_input import Cardiotocogram

class PreProcessor:
    def __init__(self):
        filename = './pipelines/standardscaler_fetalhealth.pkl'
        self.scaler = pickle.load(open(filename, 'rb'))

    def pre_process(self, cardiotocogram: Cardiotocogram):
        input_data = np.array(list(cardiotocogram.dict().values()))
        return self.scaler.transform(input_data.reshape(1, -1))