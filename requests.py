import requests

# Input data
input_data = {
  
}




# Send POST request to Flask server
response = requests.post("http://localhost:5000/predict", json=input_data)

# Check if request was successful
if response.status_code == 200:
    try:
        # Attempt to decode JSON response
        prediction = response.json()['prediction']
        print(prediction)
    except Exception as e:
        print("Error decoding JSON response:", e)
        print("Response content:", response.content)
else:
    print("Error:", response.status_code, response.reason)
    print("Response content:", response.content)
