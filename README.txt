# Disease Prediction System — College Demo

## Project files
- `main.py` — Streamlit user interface and prediction code
- `dp.pkl` — supplied trained Random Forest model
- `requirements.txt` — compatible Python package versions

## Important compatibility note
The supplied `dp.pkl` was serialized with scikit-learn **1.3.2**. It fails to predict in the inspection environment running scikit-learn 1.8.0 (`DecisionTreeClassifier` has no `monotonic_cst` attribute). Use Python **3.11** and the pinned dependencies below. Do not use Python 3.13 for this old model environment.

## Windows setup
1. Install Python 3.11 (select “Add Python to PATH” during installation).
2. Extract this ZIP into one folder.
3. Open Command Prompt in that folder.
4. Run:

```bat
py -3.11 -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
streamlit run main.py
```

5. A browser tab should open. If it does not, copy the `Local URL` shown in Command Prompt (normally `http://localhost:8501`) into your browser.

## Demo test
Try the default values first:
- Age: 25
- Heart Rate: 75
- Body Temperature: 37.0
- Oxygen Saturation: 98

Click **Predict Disease**. The result is the model's predicted class, not a medically reliable diagnosis.

## Honest project limitations
- The original training dataset and model-training script were not supplied, so model accuracy, data quality, and scientific validity have not been verified.
- The model expects four features in this exact order: Age, Heart_Rate_bpm, Body_Temperature_C, Oxygen_Saturation_%.
- A successful UI launch alone does not prove the prediction is medically accurate.
