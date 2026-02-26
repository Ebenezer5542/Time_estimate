import os
import logging
from flask import Flask, render_template, request
import joblib
import pandas as pd
from datetime import datetime, timedelta

# ── Logging ──────────────────────────────────────────────────────────────────
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "change-me-in-production")

# ── Constants ─────────────────────────────────────────────────────────────────
TRANSPORT_MODES = {
    "Trotro": 1,
    "Taxi": 2,
    "Private Vehicle": 3,
    "Walking": 4,
}

# ── Load assets once at startup ───────────────────────────────────────────────
try:
    df = pd.read_csv("towns.csv")
    towns: list[str] = df["town_name"].dropna().tolist()
    town_dict: dict[str, int] = dict(zip(df["town_name"], df["code"]))
    logger.info("Loaded %d towns from towns.csv", len(towns))
except FileNotFoundError:
    logger.error("towns.csv not found – using empty list")
    towns, town_dict = [], {}

try:
    model = joblib.load("time_estimate.pkl")
    logger.info("Model loaded successfully")
except FileNotFoundError:
    logger.error("time_estimate.pkl not found")
    model = None


# ── Helpers ───────────────────────────────────────────────────────────────────

def parse_time(raw: str) -> tuple[int, str | None]:
    """Return (seconds_since_midnight, error_message)."""
    try:
        t = datetime.strptime(raw.strip(), "%H:%M")
        return t.hour * 3600 + t.minute * 60, None
    except ValueError:
        return 0, "Invalid time – please use HH:MM (24-hour clock)."


def seconds_to_hhmm(seconds: int) -> str:
    """Convert seconds to a human-readable HH:MM string, handling >24h gracefully."""
    seconds = max(0, int(seconds))
    h, remainder = divmod(seconds, 3600)
    m = remainder // 60
    h %= 24  # wrap to same day
    period = "AM" if h < 12 else "PM"
    display_h = h if h <= 12 else h - 12
    display_h = display_h or 12
    return f"{display_h:02d}:{m:02d} {period}"


def validate_form(dep_time: str, trans_mode: str, home: str, office: str) -> list[str]:
    """Return a list of human-readable validation errors."""
    errors: list[str] = []
    if not dep_time:
        errors.append("Departure time is required.")
    if not trans_mode or trans_mode not in TRANSPORT_MODES:
        errors.append("Please select a valid transport mode.")
    if not home or home not in town_dict:
        errors.append("Please select a valid home location.")
    if not office or office not in town_dict:
        errors.append("Please select a valid office location.")
    if home and office and home == office:
        errors.append("Home and office locations cannot be the same.")
    return errors


# ── Routes ────────────────────────────────────────────────────────────────────

@app.route("/", methods=["GET", "POST"])
def index():
    arrival_time = None
    travel_duration = None
    errors: list[str] = []

    if request.method == "POST":
        dep_time   = request.form.get("dep_time", "").strip()
        trans_mode = request.form.get("trans_mode", "").strip()
        home       = request.form.get("home_location", "").strip()
        office     = request.form.get("office_location", "").strip()

        errors = validate_form(dep_time, trans_mode, home, office)

        if not errors:
            time_seconds, time_error = parse_time(dep_time)
            if time_error:
                errors.append(time_error)
            elif model is None:
                errors.append("Prediction model is not available. Please contact support.")
            else:
                features = [
                    town_dict[home],
                    town_dict[office],
                    TRANSPORT_MODES[trans_mode],
                    time_seconds,
                ]
                try:
                    predicted_seconds = float(model.predict([features])[0])
                    arrival_seconds   = time_seconds + predicted_seconds
                    arrival_time      = seconds_to_hhmm(int(arrival_seconds))

                    # Human-readable travel duration
                    dur_min = int(predicted_seconds // 60)
                    if dur_min < 60:
                        travel_duration = f"{dur_min} min"
                    else:
                        travel_duration = f"{dur_min // 60}h {dur_min % 60}m"

                    logger.info(
                        "Prediction: %s → %s via %s | arrival %s (%s)",
                        home, office, trans_mode, arrival_time, travel_duration,
                    )
                except Exception as exc:
                    logger.exception("Prediction failed: %s", exc)
                    errors.append("Could not generate a prediction. Please try again.")

    return render_template(
        "index.html",
        towns=towns,
        transport_modes=list(TRANSPORT_MODES.keys()),
        arrival_time=arrival_time,
        travel_duration=travel_duration,
        errors=errors,
        form=request.form,
    )


# ── Entry point ───────────────────────────────────────────────────────────────
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("FLASK_DEBUG", "false").lower() == "true"
    app.run(host="0.0.0.0", port=port, debug=debug)