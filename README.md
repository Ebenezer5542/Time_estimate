🔗 Live Demo: https://time-estimate.onrender.com

📌 Overview

The Time Estimator is a Flask-based web application that predicts estimated arrival time for commuters in Accra based on:

Departure time

Mode of transport

Home location

Office location

⚠️ Note:
This project was built as a machine learning mock test / prototype.
The dataset used was relatively small and collected from friends using SurveyCTO, so predictions are experimental and not production-grade.

The focus of the project was to demonstrate:

End-to-end ML workflow

Model serialization and deployment

Flask integration

UI/UX polish

Cloud deployment (Render)

🧠 Machine Learning Details

Data collected manually via SurveyCTO

Small dataset (experimental scale)

Preprocessed using Pandas

Model trained using Scikit-learn

Saved using joblib as:

time_estimate.pkl

Because of the limited dataset size, the model serves as a proof-of-concept rather than a fully optimized predictive system.

✨ Features

Modern responsive UI (Bootstrap 5)

Flatpickr time selection

Persistent form inputs after submission

Clean prediction display card

LinkedIn footer branding

Deployed on Render

🛠 Tech Stack

Backend:

Flask

Pandas

Scikit-learn

Joblib

Frontend:

Bootstrap 5 (CDN)

Flatpickr (CDN)

Font Awesome (CDN)

Deployment:

Render

Data Collection:

SurveyCTO

🚀 Running Locally
1️⃣ Clone Repository
git clone https://github.com/Ebenezer5542/time_estimate.git
cd time_estimate
2️⃣ Create Virtual Environment

Windows:

python -m venv venv
venv\Scripts\activate

Mac/Linux:

python -m venv venv
source venv/bin/activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Run App
python app.py

App will run on:

http://127.0.0.1:5000
📂 Updated File Structure
📂 TIME_ESTIMATE
│
├── app.py
├── requirements.txt
├── README.md
├── time_estimate.pkl
├── towns.csv
│
├── templates/
│   └── index.html
│
├── static/
│   └── linkedin-svgrepo-com.svg
│
└── model building/
    ├── Model Building.ipynb
    └── my_data.csv
🔍 What This Project Demonstrates

Basic ML pipeline creation

Feature preprocessing

Model persistence

Flask app integration with ML model

Clean UI integration

Deployment workflow

Git version control management

📈 Future Improvements

Collect larger, more representative dataset

Add traffic-aware features

Improve feature engineering

Implement model evaluation metrics display

Add analytics dashboard

Expand beyond Accra

📬 Contact

Ohenebeng Ebenezer

📧 ohenebengebenezer10@gmail.com

🔗 https://www.linkedin.com/in/ohenebeng-ebenezer-0190b421a
