import requests
Api_id="7dee38d3"
Api_key="4df22569469d47ced1284d7045ef9233"

WEIGHT=68
HEIGHT=179
AGE=18
GENDER='male'
exercise=input("Tell me what exercise did you do?")

Headers={
    "x-app-id": Api_id,
    "x-app-key": Api_key
}

parameters = {
    "query": exercise,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}


response=requests.get("http://status.nutritionix.com/v2/natural/exercise",json=parameters,headers=Headers)
result=response.json()
print(result)
