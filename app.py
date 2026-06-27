# from flask import Flask, render_template, request
# from predict import predict_loan

# app = Flask(__name__)


# @app.route("/")
# def home():
#     return render_template("home.html")


# @app.route("/input")
# def input_page():
#     return render_template("input.html")


# @app.route("/predict", methods=["POST"])
# def predict():

#     form_data = request.form.to_dict()

#     result, confidence = predict_loan(form_data)

#     if result == "Y":
#         prediction = "Loan Approved ✅"
#     else:
#         prediction = "Loan Rejected ❌"

#     return render_template(
#         "output.html",
#         prediction=prediction,
#         confidence=round(confidence, 2)
#     )


# if __name__ == "__main__":
#     app.run(debug=True)

"""
==========================================
SMART LENDER - FLASK APPLICATION
==========================================
Main Flask application for Loan Approval
Prediction using Machine Learning.
"""

import logging
from flask import Flask, render_template, request
from predict import predict_loan

# ==========================================
# APPLICATION CONFIGURATION
# ==========================================

app = Flask(__name__)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

# ==========================================
# HOME PAGE
# ==========================================

@app.route("/")
def home():
    return render_template("home.html")


# ==========================================
# INPUT PAGE
# ==========================================

@app.route("/input")
def input_page():
    return render_template("input.html")


# ==========================================
# PREDICTION ROUTE
# ==========================================

@app.route("/predict", methods=["POST"])
def predict():

    try:

        # Get user inputs
        form_data = request.form.to_dict()

        logging.info("Received loan application.")

        # Predict loan status
        result, confidence = predict_loan(form_data)

        # Convert prediction into user-friendly text
        if result == "Y":
            prediction = "Loan Approved"
        else:
            prediction = "Loan Rejected"

        logging.info(
            f"Prediction completed successfully. Result: {prediction}"
        )

        return render_template(
            "output.html",
            prediction=prediction,
            confidence=confidence
        )

    except ValueError as e:

        logging.error(f"Input Error: {e}")

        return render_template(
            "output.html",
            prediction="Input Error",
            confidence=0,
            error=str(e)
        ), 400

    except FileNotFoundError as e:

        logging.error(f"Model File Missing: {e}")

        return render_template(
            "output.html",
            prediction="System Error",
            confidence=0,
            error="Model files could not be found."
        ), 500

    except Exception as e:

        logging.exception("Unexpected Error")

        return render_template(
            "output.html",
            prediction="Prediction Failed",
            confidence=0,
            error=str(e)
        ), 500


# ==========================================
# START APPLICATION
# ==========================================

if __name__ == "__main__":

    logging.info("Starting Smart Lender Application...")

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )