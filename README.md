Global Food Security Predictor

A machine learning model that predicts a country's Hunger Severity Score
based on 57 real-world indicators from the World Bank and UN FAO across 217 countries.

 Built at the ML & Deep Learning Masterclass — University of Lagos
Organized in collaboration with Afretec Network.
Result: 1st Place — Model predicted 33.5 vs actual Global Hunger Index of 32.5.

---

 Project Overview
Food crises don't happen overnight. This model predicts which countries 
are heading toward food insecurity before it peaks — giving governments 
and NGOs the early warning they need to act.

---

 Model Details
- Type: Linear Regression (TensorFlow/Keras)
- Target: Hunger Severity Index (0-100 scale)
- Training MAE: 1.49
- Test MAE: 1.64 (less than 2% average error)
- Dataset: Global Food Security Intelligence — 217 countries, 57 indicators

---

 Tech Stack
- Python
- TensorFlow / Keras
- Pandas & NumPy
- Scikit-learn
- Streamlit (deployment)
- Google Colab

---

 How to Run the App
```bash
pip install streamlit tensorflow pandas numpy
streamlit run app.py
```

---

 Team — Group 2
- Mine Dema (Lala)
- Amaka
- Kofo
- Adeola
- Rima

---

## 🌐 SDG Alignment
This project directly supports **SDG 2 — Zero Hunger** by providing 
a data-driven early warning system for food insecurity.
