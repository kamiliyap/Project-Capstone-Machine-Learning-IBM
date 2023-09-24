import requests
from requests.structures import CaseInsensitiveDict

# Get access token
url = "https://iam.cloud.ibm.com/oidc/token"
headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/x-www-form-urlencoded"
data = "grant_type=urn:ibm:params:oauth:grant-type:apikey&apikey=3Iw2W6viI8zoZ0rsTa29Fq7cBgltDhv6DU_WK7vt9Ugh"
resp = requests.post(url, headers=headers, data=data)
if resp.status_code == 200:
    json_resp = resp.json()
    access_token= json_resp.get('access_token')
else:
    print("Failed to retrieve access token. Status code:", resp.status_code)
 
def prediksi():
    #Get Prediction
    url = "https://eu-gb.ml.cloud.ibm.com/ml/v4/deployments/0c2a8c67-92d3-43a3-b19b-69c4ae420e32/predictions?version=2021-05-01"
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"
    headers["Accept"] = "application/json"
    headers["Authorization"] = "Bearer " + access_token

    data = {
        "input_data": [
            {
                "fields": [
                    "Gender", "Age", "Education Level", "Institution Type", "IT Student", "Location",
                    "Load-shedding", "Financial Condition", "Internet Type", "Network Type",
                    "Class Duration", "Self Lms", "Device"
                ],
                "values": [
                    [
                        Gender_value, Age_value, Education_value, Institution_value, IT_value, Location_value,
                        Load_value, Financial_value, Internet_value, Network_value, Class_value,
                        Self_value, Device_value
                    ]
                ]
            }
        ]
    }

    resp = requests.post(url, headers=headers, json=data)

    if resp.status_code == 200:
        predictions = resp.json()
        prediction_value = predictions['predictions'][0]['values'][0][0]
        print("\n=============================== PREDICTION RESULTS =============================================")
        print("\t\t\t   "+"Adaptivity Level = "+prediction_value+"\t\t\t")
        print("================================================================================================")
    else:
        print("Error:", resp.status_code)

while(True):
    # Input data
    Gender_value=str(input("Gender= "))
    Age_value=str(input("Age= "))
    Education_value=str(input("Education Level= "))
    Institution_value=str(input("Institution Type= "))
    IT_value=str(input("IT Student= "))
    Location_value=str(input("Location= "))
    Load_value=str(input("Load-shedding= "))
    Financial_value=str(input("Financial Condition= "))
    Internet_value=str(input("Internet Type= "))
    Network_value=str(input("Network Type= "))
    Class_value=str(input("Class Duration= "))
    Self_value=str(input("Self Lms= "))
    Device_value=str(input("Device= "))

    # Call prediksi function
    prediksi()