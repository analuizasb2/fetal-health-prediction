from flask_openapi3 import OpenAPI, Info
from flask import redirect
from schema.cardiotocogram_input import Cardiotocogram
from model.pre_processor import PreProcessor
from model.model import FetalHealthClassifier

info = Info(title="Fetal Health Classifier", version="1.0.0")
app = OpenAPI(__name__, info=info)

pre_processor = PreProcessor()
classifier = FetalHealthClassifier()

@app.get("/")
def home():
    """Documentação.
    """
    return redirect('/openapi/swagger')

@app.post("/classify")
def classify(body: Cardiotocogram):
    """Classifica a saúde fetal.
    """
    input_preprocessed = pre_processor.pre_process(body)
    classification = classifier.classify_patient(input_preprocessed)
    return {"classification": classification[0]}
