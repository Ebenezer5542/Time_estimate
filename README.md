# Accra Commute Estimator

## Overview
The **Accra Commute Estimator** is a Streamlit web application that predicts the estimated arrival time for commuters in Accra based on:
- Departure time
- Mode of transport
- Home location
- Office location

The application uses a trained machine learning model to make predictions based on historical commute data.

## Features
- **User Input:** Select your town and enter your departure time.
- **Real-Time Prediction:** Get an estimated time of arrival based on your inputs.
- **Data Processing:** Converts user inputs into numerical formats that the model understands.
- **Model Integration:** Uses a pre-trained model to make accurate commute time predictions.

## Installation
### **1. Clone the Repository**
```sh
git clone https://github.com/yourusername/time_estimate.git
cd time_estimate
```
### **2. Install Dependencies**
Make sure you have Python installed, then install the required packages:
```sh
pip install -r requirements.txt
```

## Running the App Locally
Run the following command to start the Streamlit app:
```sh
streamlit run app.py
```

## Deployment on Streamlit Cloud
This app is deployed on [Streamlit Cloud](https://share.streamlit.io). To deploy your own version:
1. Push the latest code to GitHub.
2. Go to [Streamlit Cloud](https://streamlit.io/cloud) and create a new app.
3. Select your GitHub repository and deploy.

## File Structure
```
📂 time_estimate
│-- app.py               # Main Streamlit app
│-- time_estimate.pkl    # Trained machine learning model
│-- towns.csv            # Town names and corresponding codes
│-- requirements.txt     # Dependencies
│-- README.md            # Project documentation
```

## Requirements
- Streamlit
- Pandas
- Joblib
- Scikit-learn

## Future Improvements
- Adding real-time traffic data for better predictions.
- Enhancing the user interface.
- Expanding to more locations beyond Accra.

## License
This project is open-source.

## Contact
For any questions or contributions, feel free to reach out:
- **Email:** ohenebengebenezer10@gmail.com
- **GitHub:** Ebenezer5542(https://github.com/Ebenezer5542)

