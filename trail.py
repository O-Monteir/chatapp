import os
import rasa
from rasa.model import get_model

    # Load the Rasa model
model_path = "extracted_model.pkl"  # Replace with the actual path to your model
model_directory = os.path.abspath(model_path)
model = get_model(model_directory)

# Create a Rasa interpreter
interpreter = rasa.nlu.model.Interpreter.load(model)

# Run the Rasa model
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break

    # Get Rasa model response
    response = interpreter.parse(user_input)
    print("Bot:", response['text'])

    


# import requests

# # Define the endpoint URL of your Rasa model deployed on Render
# rasa_endpoint = "https://rasa-model.onrender.com/webhooks/rest/webhook"

# # The message you want to send to the Rasa chatbot
# user_message = "Hi"

# # Create a dictionary payload with the user message
# payload = {
#     "message": user_message
# }

# try:
#     # Send a POST request to the Rasa model endpoint with the user message
#     response = requests.post(rasa_endpoint, json=payload)
#     print(response)
#     # Check if the request was successful (HTTP status code 200)
#     if response.status_code == 200:
#         # Print the response from the Rasa chatbot
#         print("Bot Response:")
       
#         print(response.json())  # Assuming the response is in JSON format
#     else:
#         print("Request failed with status code:", response.status_code)

# except requests.RequestException as e:
#     print("Request Exception:", e)
