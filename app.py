import os
from flask import Flask, render_template, request
import joblib
import pandas as pd
from datetime import datetime, timedelta

app = Flask(__name__)

# Load data and model
df = pd.read_csv("towns.csv")
towns = df["town_name"].tolist()
town_dict = dict(zip(df["town_name"], df["code"]))
model = joblib.load("time_estimate.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    arrival_time = None
    error_message = None

    if request.method == "POST":
        dep_time = request.form.get("dep_time", "").strip()
        trans_mode = request.form.get("trans_mode", "").strip()
        home_select = request.form.get("home_location", "").strip()
        office_select = request.form.get("office_location", "").strip()

        # Validate time
        try:
            time_obj = datetime.strptime(dep_time, "%H:%M")
            time_in_seconds = time_obj.hour * 3600 + time_obj.minute * 60
        except ValueError:
            error_message = "Invalid time format! Use HH:MM (24-hour format)"
            return render_template(
                "index.html",
                towns=towns,
                arrival_time=None,
                error_message=error_message,
                request=request
            )

        # Convert selections to codes
        home_code = town_dict.get(home_select)
        office_code = town_dict.get(office_select)
        mode_map = {"Trotro": 1, "Taxi": 2, "Private Vehicle": 3, "Walking": 4}
        mode = mode_map.get(trans_mode)

        if None in [home_code, office_code, mode]:
            error_message = "Please select valid options for all fields."
            return render_template(
                "index.html",
                towns=towns,
                arrival_time=None,
                error_message=error_message,
                request=request
            )

        # Predict arrival time
        features = [home_code, office_code, mode, time_in_seconds]
        prediction = model.predict([features])
        ar_time = int(prediction + time_in_seconds)
        arrival_time = str(timedelta(seconds=ar_time)).split('.')[0]  # HH:MM:SS

    return render_template(
        "index.html",
        towns=towns,
        arrival_time=arrival_time,
        error_message=error_message,
        request=request
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)


