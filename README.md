# Accra Commute Estimator

## Overview
The **Accra Commute Estimator** is a Flask-based web application that predicts the estimated arrival time for commuters in Accra based on:
- Departure time (via a modern time picker)
- Mode of transport
- Home location
- Office location

🔗 **Try it here:** [Live App on Render](https://time-estimate.onrender.com)
The application uses a trained machine learning model to make predictions based on historical commute data.

## Features
- **User-Friendly UI:** Modern Bootstrap interface with a responsive card layout and iconography.
- **Smart Time Input:** JavaScript-powered time picker (Flatpickr) for easy selection.
- **Real-Time Prediction:** Get an estimated time of arrival instantly after submitting details.
- **Persistent Form Values:** All inputs remain visible after prediction for easy adjustments.
- **Model Integration:** Uses a pre-trained model to make accurate commute time predictions.

## Installation

### **1. Clone the Repository**
```sh
git clone https://github.com/yourusername/time_estimate.git
cd time_estimate
```

### **2. Create Virtual Environment (Recommended)**
```sh
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows
```

### **3. Install Dependencies**
```sh
pip install -r requirements.txt
```

## Running the App Locally
Run the following command to start the Flask app:
```sh
python app.py
```
Open your browser and visit:
```
http://127.0.0.1:5000/
```

## Deployment
You can deploy this app on:
- **Render** (recommended for quick Flask deployment)
- **Heroku** (requires a `Procfile`)
- **PythonAnywhere**
- **Any VPS or cloud hosting** that supports Python/Flask

## File Structure
```
📂 time_estimate
│-- app.py               # Main Flask app
│-- templates/
│   └── index.html        # Modern Bootstrap + Flatpickr UI
│-- static/               # Static assets (optional)
│-- time_estimate.pkl     # Trained machine learning model
│-- towns.csv             # Town names and corresponding codes
│-- requirements.txt      # Dependencies
│-- README.md             # Project documentation
```

## Requirements
- Flask
- Pandas
- Joblib
- Scikit-learn
- Bootstrap 5 (CDN in HTML)
- Flatpickr (CDN in HTML)
- Font Awesome (CDN in HTML)

## Future Improvements
- Integrate **real-time traffic data** for more accurate predictions.
- Add **summary cards** showing all selected inputs alongside results.
- Support **multiple cities** beyond Accra.
- Add **multi-step form flow** for a more app-like experience.

## License
This project is open-source.

## Contact
For any questions or contributions, feel free to reach out:
- **Email:** ohenebengebenezer10@gmail.com
- **GitHub:** [Ebenezer5542](https://github.com/Ebenezer5542)
