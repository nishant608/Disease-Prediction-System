import pickle
import warnings
from pathlib import Path

import streamlit as st

warnings.filterwarnings("ignore")

# ---------------- Page configuration ----------------
st.set_page_config(
    page_title="MediPredict | Disease Prediction",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------- Styling ----------------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@600;700;800&display=swap');

    :root {
        --navy: #102a43;
        --blue: #1769aa;
        --cyan: #23a6b8;
        --muted: #627d98;
        --line: #d9e6f2;
    }

    .stApp {
        background:
            radial-gradient(circle at 8% 5%, rgba(35,166,184,.10), transparent 26%),
            linear-gradient(135deg, #f5f9fd 0%, #edf5fb 55%, #f8fbfe 100%);
        font-family: 'DM Sans', sans-serif;
    }

    [data-testid="stHeader"] { background: rgba(245,249,253,.75); }
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #102a43 0%, #164e72 100%);
    }
    [data-testid="stSidebar"] * { color: #f4f9ff !important; }
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {
        color: #d7e8f5 !important;
    }

    .block-container {
        max-width: 1180px;
        padding-top: 2rem;
        padding-bottom: 2.5rem;
    }

    .hero {
        background: linear-gradient(115deg, #102a43 0%, #1769aa 58%, #23a6b8 100%);
        padding: 30px 34px;
        border-radius: 22px;
        color: white;
        box-shadow: 0 14px 35px rgba(16, 42, 67, .16);
        margin-bottom: 22px;
    }
    .hero-kicker {
        color: #c9f3f3;
        text-transform: uppercase;
        letter-spacing: 2px;
        font-size: 11px;
        font-weight: 700;
        margin-bottom: 8px;
    }
    .hero h1 {
        color: white;
        font-family: 'Manrope', sans-serif;
        font-size: clamp(28px, 4vw, 42px);
        line-height: 1.15;
        margin: 0 0 8px 0;
        font-weight: 800;
    }
    .hero p {
        color: #e1f0fa;
        font-size: 15px;
        margin: 0;
        max-width: 680px;
    }
    .hero-chip {
        display: inline-block;
        margin-top: 17px;
        padding: 6px 12px;
        border: 1px solid rgba(255,255,255,.3);
        border-radius: 30px;
        color: #effcff;
        font-size: 12px;
        background: rgba(255,255,255,.10);
    }

    .section-label {
        color: #1769aa;
        font-size: 12px;
        font-weight: 800;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        margin: 5px 0 5px 0;
    }
    .section-heading {
        color: #102a43;
        font-family: 'Manrope', sans-serif;
        font-size: 23px;
        font-weight: 800;
        margin: 0 0 4px 0;
    }
    .section-help {
        color: #627d98;
        font-size: 14px;
        margin-bottom: 14px;
    }

    div[data-testid="stVerticalBlockBorderWrapper"] {
        background: rgba(255,255,255,.88);
        border: 1px solid #dce8f2;
        border-radius: 18px;
        box-shadow: 0 8px 24px rgba(16,42,67,.055);
    }

    div[data-testid="stNumberInput"] label,
    div[data-testid="stSelectbox"] label {
        color: #243b53 !important;
        font-weight: 700 !important;
        font-size: 13px !important;
    }

    div[data-testid="stNumberInput"] input {
        border-radius: 10px !important;
        background: #f8fbfe !important;
    }

    .stButton > button, div[data-testid="stFormSubmitButton"] > button {
        width: 100%;
        min-height: 48px;
        border: 0;
        border-radius: 12px;
        color: white;
        font-weight: 700;
        background: linear-gradient(100deg, #1769aa, #23a6b8);
        box-shadow: 0 7px 16px rgba(23,105,170,.20);
        transition: transform .15s ease, box-shadow .15s ease;
    }
    .stButton > button:hover, div[data-testid="stFormSubmitButton"] > button:hover {
        color: white;
        transform: translateY(-1px);
        box-shadow: 0 10px 20px rgba(23,105,170,.25);
    }

    .result-label {
        color: #1769aa;
        font-size: 12px;
        font-weight: 800;
        letter-spacing: 1.4px;
        text-transform: uppercase;
    }
    .result-name {
        color: #102a43;
        font-family: 'Manrope', sans-serif;
        font-size: 30px;
        font-weight: 800;
        margin: 5px 0 8px 0;
    }
    .result-note {
        color: #627d98;
        font-size: 13px;
    }
    .small-note {
        color: #627d98;
        font-size: 12px;
    }
    footer { visibility: hidden; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------- Model loader ----------------
@st.cache_resource
def load_model(model_path: str):
    with open(model_path, "rb") as model_file:
        return pickle.load(model_file)


# ---------------- Sidebar ----------------
with st.sidebar:
    st.markdown("## 🩺 MediPredict")
    st.markdown("**Disease Prediction System**")
    st.markdown("---")
    st.markdown("### About this project")
    st.markdown(
        "An academic machine-learning demonstration that uses four "
        "health measurements as model inputs."
    )
    st.markdown("---")
    st.markdown("### Healthy habits")
    st.markdown(
        "- Stay hydrated\n"
        "- Eat a balanced diet\n"
        "- Get regular physical activity\n"
        "- Maintain a regular sleep schedule\n"
        "- Consult a qualified professional for health concerns"
    )
    st.markdown("---")
    st.caption("Academic demo • Python + Streamlit")

# ---------------- Main header ----------------
st.markdown(
    """
    <div class="hero">
        <div class="hero-kicker">Machine learning · Academic demonstration</div>
        <h1>Health insights, made simple.</h1>
        <p>
            Enter the patient's basic health measurements to see the class
            predicted by the demonstration model.
        </p>
        <span class="hero-chip">🛡️ Educational use only — not a medical diagnosis</span>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------------- Main layout ----------------
left, right = st.columns([1.35, 0.85], gap="large")

with left:
    st.markdown('<div class="section-label">Patient information</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-heading">Enter health measurements</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-help">Fill in all four values, then run the prediction.</div>',
        unsafe_allow_html=True,
    )

    with st.container(border=True):
        with st.form("prediction_form"):
            col1, col2 = st.columns(2)
            with col1:
                age = st.number_input("Age (years)", min_value=1, max_value=120, value=25, step=1)
                heart_rate = st.number_input(
                    "Heart rate (bpm)", min_value=30, max_value=220, value=75, step=1
                )
            with col2:
                temperature = st.number_input(
                    "Body temperature (°C)",
                    min_value=30.0,
                    max_value=45.0,
                    value=37.0,
                    step=0.1,
                    format="%.1f",
                )
                oxygen = st.number_input(
                    "Oxygen saturation (%)",
                    min_value=50,
                    max_value=100,
                    value=98,
                    step=1,
                )

            st.markdown("<br>", unsafe_allow_html=True)
            submitted = st.form_submit_button("Run disease prediction  →", use_container_width=True)

with right:
    st.markdown('<div class="section-label">Input guide</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-heading">What you are entering</div>', unsafe_allow_html=True)
    with st.container(border=True):
        st.markdown("**Age**")
        st.caption("Patient's age in years.")
        st.markdown("---")
        st.markdown("**Heart rate**")
        st.caption("Beats per minute (bpm).")
        st.markdown("---")
        st.markdown("**Body temperature**")
        st.caption("Temperature in degrees Celsius.")
        st.markdown("---")
        st.markdown("**Oxygen saturation**")
        st.caption("SpO₂ percentage, as provided by a pulse oximeter.")

# ---------------- Prediction result ----------------
if submitted:
    model_path = Path(__file__).resolve().parent / "dp.pkl"

    if not model_path.exists():
        st.error("Model file 'dp.pkl' was not found. Keep dp.pkl in the same folder as main.py.")
    else:
        try:
            model = load_model(str(model_path))
            prediction = model.predict([[age, heart_rate, temperature, oxygen]])[0]

            st.markdown("")
            st.markdown('<div class="section-label">Model output</div>', unsafe_allow_html=True)
            with st.container(border=True):
                st.markdown('<div class="result-label">Predicted class</div>', unsafe_allow_html=True)
                st.markdown(
                    f'<div class="result-name">{prediction}</div>',
                    unsafe_allow_html=True,
                )
                st.markdown(
                    '<div class="result-note">This is the output generated by the supplied machine-learning model. '
                    'It is not a confirmed diagnosis or a substitute for medical advice.</div>',
                    unsafe_allow_html=True,
                )
        except Exception as error:
            st.error(
                "The model could not generate a prediction. Check that dp.pkl is the "
                "matching model file and that the pinned requirements are installed."
            )
            st.exception(error)

# ---------------- Disclaimer and footer ----------------
st.markdown("")
st.warning(
    "Important: This project is an academic demonstration. Its predictions have not "
    "been established as clinically reliable. Do not use them to diagnose, treat, or "
    "make healthcare decisions. Consult a qualified medical professional."
)
st.markdown(
    """
    <div style="text-align:center; padding:18px 0 4px 0; color:#7890a5; font-size:12px;">
        MediPredict · Built with Python and Streamlit
    </div>
    """,
    unsafe_allow_html=True,
)
