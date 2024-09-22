import os
import pandas as pd
from model.pre_processor import PreProcessor
from model.model import FetalHealthClassifier
from sklearn.metrics import accuracy_score
from schema.cardiotocogram_input import Cardiotocogram
from typing import List

pre_processor = PreProcessor()
classifier = FetalHealthClassifier()

X_test_data_path = "./X_test_dataset.csv"
X_test_data_path = os.path.join(os.path.dirname(__file__), 'X_test_dataset.csv')
Y_test_data_path = "./Y_test_dataset.csv"
Y_test_data_path = os.path.join(os.path.dirname(__file__), 'Y_test_dataset.csv')

def test_model_accuracy():
    # arrange
    x_test_dataset = pd.read_csv(X_test_data_path, delimiter=',')
    x_test_dataset = x_test_dataset.rename(columns={'baseline value': 'baseline_value'}) # rename to match schema
    x_test = x_test_dataset.values
    y_test_dataset = pd.read_csv(Y_test_data_path, delimiter=',')
    y_test = y_test_dataset.values
    cardiotocograms: List[Cardiotocogram] = [    
    Cardiotocogram(**row.to_dict())
    for _, row in x_test_dataset.iterrows()
]
    # act
    scaled_x_test = pre_processor.pre_process_patients(cardiotocograms)    
    predictions = classifier.classify_patient(scaled_x_test)
    accuracy = accuracy_score(y_test, predictions)

    # assert
    assert accuracy > 0.85