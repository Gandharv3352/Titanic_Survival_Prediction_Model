from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import pickle
import pandas as pd

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Load model
with open("titanic_pipeline.pkl", "rb") as f:
    model = pickle.load(f)

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict", response_class=HTMLResponse)
async def predict(request: Request):
    form = await request.form()

    data = pd.DataFrame([{
        "Pclass": int(form["Pclass"]),
        "Sex": form["Sex"],
        "Age": float(form["Age"]),
        "Fare": float(form["Fare"]),
        "Embarked": form["Embarked"],
        "family_size_group": int(form["family_size_group"])
    }])

    prediction = model.predict(data)[0]
    probability = model.predict_proba(data)[0][1]

    result = "Survived" if prediction == 1 else "Did not survive"

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "result": result,
            "probability": round(probability, 2)
        }
    )
