from flask import Flask, request, render_template, jsonify
import requests
import subprocess
import time

app = Flask(__name__, template_folder='Templates')

# Rasa server URL
RASA_SERVER_URL = 'http://localhost:5005/webhooks/rest/webhook'

# Initialize empty chat history
chat_history = []

def check_rasa_running():
    try:
        res = requests.get('http://localhost:5005/')
        if res.status_code == 200:
            return True
    except requests.ConnectionError:
        return False

# Start Rasa server
rasa_process = subprocess.Popen(['rasa', 'run', '-m', 'models', '--enable-api'])

# Check if Rasa server is running
while not check_rasa_running():
    print("Waiting for Rasa server to start...")
    time.sleep(5)  # Adjust the delay time as needed

print("Rasa server is now running!")

def get_bot_response(user_input):
    data = {"sender": "User", "message": user_input}
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    res = requests.post(RASA_SERVER_URL, json=data, headers=headers)
    response = res.json()
    return response[0]['text']

@app.route('/', methods=['POST', 'GET'])
def index():
    global chat_history

    if request.method == 'GET':
        return render_template('index.html', chat_history=chat_history)

    if request.method == 'POST':
        user_input = request.form['text']

        # Append user input to chat history
        chat_history.append({"message": user_input, "sender": "User"})

        # Get bot response from Rasa
        bot_response = get_bot_response(user_input)

        # Append bot response to chat history
        chat_history.append({"message": bot_response, "sender": "Bot"})

        return render_template('index.html', chat_history=chat_history)

# Endpoint to get bot response
@app.route('/get_bot_response', methods=['POST'])
def get_bot_response_route():
    user_input = request.json.get('text')
    bot_response = get_bot_response(user_input)
    return jsonify({'bot_response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)



# from flask import Flask, request, render_template, jsonify
# import requests
# import json

# app = Flask(__name__, template_folder='Templates')

# # Rasa server URL
# RASA_SERVER_URL = 'http://localhost:5005/webhooks/rest/webhook'

# # Initialize empty chat history
# chat_history = []

# def get_bot_response(user_input):
#     data = json.dumps({"sender": "User", "message": user_input})
#     headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
#     res = requests.post(RASA_SERVER_URL, data=data, headers=headers)
#     response = res.json()
#     return response[0]['text']

# @app.route('/', methods=['POST', 'GET'])
# def index():
#     global chat_history

#     if request.method == 'GET':
#         return render_template('index.html', chat_history=chat_history)

#     if request.method == 'POST':
#         user_input = request.form['text']

#         # Append user input to chat history
#         chat_history.append({"message": user_input, "sender": "User"})

#         # Get bot response from Rasa
#         bot_response = get_bot_response(user_input)

#         # Append bot response to chat history
#         chat_history.append({"message": bot_response, "sender": "Bot"})

#         return render_template('index.html', chat_history=chat_history)

# # Endpoint to get bot response
# @app.route('/get_bot_response', methods=['POST'])
# def get_bot_response_route():
#     user_input = request.json.get('text')
#     bot_response = get_bot_response(user_input)
#     return jsonify({'bot_response': bot_response})

# if __name__ == '__main__':
#     app.run(debug=True)


# # from flask import Flask, request, render_template
# # import requests
# # import json

# # app = Flask(__name__, template_folder='Templates')

# # # Rasa server URL
# # RASA_SERVER_URL = 'http://localhost:5005/webhooks/rest/webhook'

# # # Initialize empty chat history
# # chat_history = []

# # def get_bot_response(user_input):
# #     data = json.dumps({"sender": "User", "message": user_input})
# #     headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
# #     res = requests.post(RASA_SERVER_URL, data=data, headers=headers)
# #     response = res.json()
# #     return response[0]['text']

# # @app.route('/', methods=['POST', 'GET'])
# # def index():
# #     global chat_history

# #     if request.method == 'GET':
# #         return render_template('index.html', chat_history=chat_history)

# #     if request.method == 'POST':
# #         user_input = request.form['text']

# #         # Append user input to chat history
# #         chat_history.append({"message": user_input, "sender": "User"})

# #         # Get bot response from Rasa
# #         bot_response = get_bot_response(user_input)

# #         # Append bot response to chat history
# #         chat_history.append({"message": bot_response, "sender": "Bot"})

# #         return render_template('index.html', chat_history=chat_history)

# # if __name__ == '__main__':
# #     app.run(debug=True)
