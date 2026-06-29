"""
==========================================
SMART LENDER - PREDICTION MODULE
==========================================
Loads the trained model and preprocessing
objects, processes user input, and returns
the loan prediction.
"""

import joblib
import numpy as np

# ==========================================
# LOAD MODEL AND PREPROCESSING OBJECTS
# ==========================================

try:
    model_artifacts = joblib.load("models/best_loan_model.pkl")
    preprocessing = joblib.load("models/preprocessed_loan_data.pkl")

    model = model_artifacts["model"]
    scaler = model_artifacts["scaler"]
    label_encoders = preprocessing["label_encoders"]

except FileNotFoundError as e:
    raise FileNotFoundError(
        f"Required model file not found: {e}"
    )

except Exception as e:
    raise Exception(
        f"Error loading model files: {e}"
    )


# ==========================================
# PREDICTION FUNCTION
# ==========================================

def predict_loan(form_data):
    """
    Predict loan approval based on form input.

    Parameters
    ----------
    form_data : dict
        Dictionary containing values submitted
        from the HTML form.

    Returns
    -------
    tuple
        (prediction, confidence)
    """

    try:

        # ==============================
        # Encode categorical variables
        # ==============================

        gender = label_encoders["Gender"].transform(
            [form_data["Gender"]]
        )[0]

        married = label_encoders["Married"].transform(
            [form_data["Married"]]
        )[0]

        dependents = label_encoders["Dependents"].transform(
            [form_data["Dependents"]]
        )[0]

        education = label_encoders["Education"].transform(
            [form_data["Education"]]
        )[0]

        self_employed = label_encoders["Self_Employed"].transform(
            [form_data["Self_Employed"]]
        )[0]

        property_area = label_encoders["Property_Area"].transform(
            [form_data["Property_Area"]]
        )[0]

        # ==============================
        # Numerical variables
        # ==============================

        applicant_income = float(form_data["ApplicantIncome"])

        coapplicant_income = float(
            form_data["CoapplicantIncome"]
        )

        loan_amount = float(
            form_data["LoanAmount"]
        )

        loan_amount_term = float(
            form_data["Loan_Amount_Term"]
        )

        credit_history = float(
            form_data["Credit_History"]
        )

        # ==============================
        # Feature Vector
        # ==============================

        features = np.array([[
            gender,
            married,
            dependents,
            education,
            self_employed,
            applicant_income,
            coapplicant_income,
            loan_amount,
            loan_amount_term,
            credit_history,
            property_area
        ]])

        # ==============================
        # Scale Features
        # ==============================

        features_scaled = scaler.transform(features)

        # ==============================
        # Prediction
        # ==============================

        prediction = model.predict(features_scaled)[0]

        probability = model.predict_proba(
            features_scaled
        )[0]

        confidence = round(
            np.max(probability) * 100,
            2
        )

        # ==============================
        # Decode Output
        # ==============================

        result = label_encoders[
            "Loan_Status"
        ].inverse_transform(
            [prediction]
        )[0]

        return result, confidence

    except KeyError as e:
        raise ValueError(
            f"Missing input field: {e}"
        )

    except ValueError as e:
        raise ValueError(
            f"Invalid numeric input: {e}"
        )

    except Exception as e:
        raise Exception(
            f"Prediction failed: {e}"
        )