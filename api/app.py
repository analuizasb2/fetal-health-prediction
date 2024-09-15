from flask_openapi3 import OpenAPI, Info
from flask import redirect

info = Info(title="Fetal Health Classifier", version="1.0.0")
app = OpenAPI(__name__, info=info)

@app.get("/")
def home():
    """Documentação.
    """
    return redirect('/openapi/swagger')

@app.post("/classify")
def classify():
    """Classifica a saúde fetal.
    """
    return {"classification": "Normal"}
