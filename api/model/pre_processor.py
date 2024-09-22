import numpy as np
import pickle
from schema.cardiotocogram_input import Cardiotocogram

class PreProcessor:
    def __init__(self):
        filename = './pipelines/standardscaler_fetalhealth.pkl'
        self.scaler = pickle.load(open(filename, 'rb'))

    def pre_process_patient(self, cardiotocogram: Cardiotocogram):
        input_data = np.array(list(cardiotocogram.model_dump().values()))
        return self.scaler.transform(input_data.reshape(1, -1))
    
    def pre_process_patients(self, cardiotocograms: list[Cardiotocogram]):
        input_data = np.array([list(c.model_dump().values()) for c in cardiotocograms])
        return self.scaler.transform(input_data)