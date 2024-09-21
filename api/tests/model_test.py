import sys
print(sys.path)  # This will show you the current Python path
from model.pre_processor import PreProcessor
from model.model import FetalHealthClassifier
import pandas as pd
from sklearn.metrics import accuracy_score

pre_processor = PreProcessor()
classifier = FetalHealthClassifier()

X_test_data_path = "./X_test_dataset.csv"
Y_test_data_path = "./Y_test_dataset.csv"

def test_addition():
    assert 1 + 1 == 2

def test_model_accuracy():
    # arrange
    x_test_dataset = pd.read_csv(X_test_data_path, delimiter=',')
    x_test = x_test_dataset.values
    y_test_dataset = pd.read_csv(Y_test_data_path, delimiter=',')
    y_test = y_test_dataset.values

    # act
    scaled_x_test = pre_processor.pre_process(x_test)
    predictions = classifier.classify_patient(scaled_x_test)
    accuracy = accuracy_score(y_test, predictions)

    # assert
    print(accuracy)
    assert accuracy > 0.8