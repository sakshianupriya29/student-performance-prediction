from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained machine learning model
model = joblib.load("model/student_performance_model.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    # Get data from the web form
    data = {
        "school": request.form["school"],
        "sex": request.form["sex"],
        "age": int(request.form["age"]),
        "address": request.form["address"],
        "famsize": request.form["famsize"],
        "Pstatus": request.form["Pstatus"],
        "Medu": int(request.form["Medu"]),
        "Fedu": int(request.form["Fedu"]),
        "Mjob": request.form["Mjob"],
        "Fjob": request.form["Fjob"],
        "reason": request.form["reason"],
        "guardian": request.form["guardian"],
        "traveltime": int(request.form["traveltime"]),
        "studytime": int(request.form["studytime"]),
        "failures": int(request.form["failures"]),
        "schoolsup": request.form["schoolsup"],
        "famsup": request.form["famsup"],
        "paid": request.form["paid"],
        "activities": request.form["activities"],
        "nursery": request.form["nursery"],
        "higher": request.form["higher"],
        "internet": request.form["internet"],
        "romantic": request.form["romantic"],
        "famrel": int(request.form["famrel"]),
        "freetime": int(request.form["freetime"]),
        "goout": int(request.form["goout"]),
        "Dalc": int(request.form["Dalc"]),
        "Walc": int(request.form["Walc"]),
        "health": int(request.form["health"]),
        "absences": int(request.form["absences"])
    }

    # Convert input into DataFrame
    input_data = pd.DataFrame([data])

    # Make prediction
    prediction = model.predict(input_data)[0]

    # Keep prediction within grade range
    prediction = max(0, min(20, prediction))

    return render_template(
        "index.html",
        prediction=round(prediction, 2)
    )


if __name__ == "__main__":
    app.run(debug=True)