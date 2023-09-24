from flask import Flask, request, render_template
import requests
from requests.structures import CaseInsensitiveDict
from flask import json
import json

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    prediction_data = False

    if request.method == "POST":
        print(request.form["Provinsi"])
        print(request.form["Tahun"])
        print(request.form["Produksi"])
        print(request.form["Luas Panen"])
        print(request.form["Curah hujan"])
        print(request.form["Kelembapan"])
        print(request.form["Suhu rata-rata"])
        Provinsi_value = request.form["Provinsi"]
        Tahun_value = request.form["Tahun"]
        Produksi_value = request.form["Produksi"]
        Luas_Panen_value = request.form["Luas Panen"]
        Curah_hujan_value = request.form["Curah hujan"]
        Kelembapan_value = request.form["Kelembapan"]
        Suhu_rata_rata_value = request.form["Suhu rata-rata"]

        access_token = get_access_token()

        prediction_value = get_prediction(
            access_token,
            Provinsi_value,
            Tahun_value,
            Produksi_value,
            Luas_Panen_value,
            Curah_hujan_value,
            Kelembapan_value,
            Suhu_rata_rata_value,
            )

        prediction_data = prediction_value
    return render_template("index.html", prediction=prediction_data)


def get_access_token():
    url = "https://iam.cloud.ibm.com/identity/token"
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/x-www-form-urlencoded"
    data = "grant_type=urn:ibm:params:oauth:grant-type:apikey&apikey=6NEMsB77hCoV1KP5an_z2sq1y3EA9f-u2MxcQJu0Vdyd"
    resp = requests.post(url, headers=headers, data=data)
    if resp.status_code == 200:
        json_resp = resp.json()
        return json_resp.get("access_token")
    else:
        return None


def get_prediction(access_token, *input_values):
    url = "https://us-south.ml.cloud.ibm.com/ml/v4/deployments/fc1817cf-8af3-4430-8e57-3d20de967b7b/predictions?version=2021-05-01"
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"
    headers["Accept"] = "application/json"
    headers["Authorization"] = "Bearer " + access_token

    data = {
        "input_data": [
            {
                "fields": [
                    "Provinsi",
                    "Tahun",
                    "Produksi",
                    "Luas Panen",
                    "Curah hujan",
                    "Kelembapan",
                    "Suhu rata-rata",
                ],
                "values": [list(input_values)],
            }
        ]
    }

    resp = requests.post(url, headers=headers, json=data)

    if resp.status_code == 200:
        predictions = resp.json()
        prediction_value = predictions["predictions"][0]["values"][0][0]
        output = json.loads(resp.text)
        print("output >>", output)
        return prediction_value
    else:
        return None


# Uncomment code below if you want to host it locally
if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")


# Made by O. Midiyanto in IBM Academy with Infinite Learning - 2023
# Heart Disease Predict Prediction Web - by Dicky Wahyudi -2023 :D
