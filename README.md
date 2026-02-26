# 🕐 TravelCast — Commute Arrival Predictor

> A Flask-based machine learning web app that predicts your estimated arrival time based on departure time, transport mode, and location — built for commuters in Accra, Ghana.

🔗 **Live Demo:** [time-estimate.onrender.com](https://time-estimate.onrender.com)

---

## 📌 Overview

TravelCast is an end-to-end machine learning project that takes a commuter's inputs and returns a predicted arrival time. It was built as a **proof-of-concept prototype** to demonstrate a complete ML workflow — from data collection to cloud deployment.

> ⚠️ **Note:** The dataset was collected from a small group of volunteers via SurveyCTO, so predictions are experimental rather than production-grade. The primary goal of this project is to showcase the full pipeline: data collection → model training → Flask integration → deployment.

---

## ✨ Features

- ⏱ Departure time selection via Flatpickr (24-hour format)
- 🚌 Multiple transport modes: Trotro, Taxi, Private Vehicle, Walking
- 📍 Dropdowns for home and office locations across Accra
- 🤖 ML-powered arrival time prediction
- 📱 Responsive UI with persistent form state after submission
- ☁️ Deployed and accessible via Render

---

## 🧠 Machine Learning Details

| Property | Details |
|---|---|
| Data collection | SurveyCTO (manual, from volunteers) |
| Dataset size | Small / experimental scale |
| Preprocessing | Pandas |
| Model framework | Scikit-learn |
| Model serialization | Joblib (`.pkl`) |

Because of the limited dataset size, this model is a **proof-of-concept** — not a fully optimized predictive system. See [Future Improvements](#-future-improvements) for the roadmap.

---

## 🛠 Tech Stack

**Backend** — Flask · Pandas · Scikit-learn · Joblib

**Frontend** — Bootstrap 5 · Flatpickr · Font Awesome (all via CDN)

**Deployment** — Render

**Data Collection** — SurveyCTO

---

## 🚀 Running Locally

### 1. Clone the repository

```bash
git clone https://github.com/Ebenezer5542/time_estimate.git
cd time_estimate
```

### 2. Create and activate a virtual environment

**Windows**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac / Linux**
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
python app.py
```

The app will be available at **http://127.0.0.1:5000**

---

## 📂 Project Structure

```
TIME_ESTIMATE/
├── app.py                    # Flask application & prediction logic
├── requirements.txt
├── README.md
├── time_estimate.pkl         # Trained ML model
├── towns.csv                 # Location data with encoded town codes
│
├── templates/
│   └── index.html            # Main UI template (Jinja2)
│
├── static/
│   └── linkedin-svgrepo-com.svg
│
└── model building/
    ├── Model Building.ipynb  # Training notebook
    └── my_data.csv           # Raw collected data
```

---

## 🔍 What This Project Demonstrates

- End-to-end ML pipeline (collection → preprocessing → training → deployment)
- Feature engineering with categorical encoding
- Model persistence with Joblib
- Flask integration with a trained Scikit-learn model
- Responsive frontend with Jinja2 templating
- Cloud deployment via Render
- Git-based version control workflow

---

## 📈 Future Improvements

- [ ] Collect a larger, more representative dataset
- [ ] Incorporate real-time traffic data
- [ ] Add model evaluation metrics to the UI
- [ ] Improve feature engineering (time of day, day of week, weather)
- [ ] Build an analytics dashboard for prediction history
- [ ] Expand coverage beyond Accra

---

## 📬 Contact

**Ohenebeng Ebenezer**
📧 [ohenebengebenezer10@gmail.com](mailto:ohenebengebenezer10@gmail.com)
🔗 [linkedin.com/in/ohenebeng-ebenezer-0190b421a](https://www.linkedin.com/in/ohenebeng-ebenezer-0190b421a)
