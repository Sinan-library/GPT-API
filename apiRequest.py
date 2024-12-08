import requests
import json
import time

API_ENDPOINT = "https://api.openai.com/v1/chat/completions"
HEADERS = {
    "Authorization": "Bearer YOUR_API_KEY_HERE",
    "Content-Type": "application/json"
}

def chat_with_gpt():
    payload = {
    "model": "gpt-3.5-turbo",
    "messages": [
        {"role": "system", "content": "Thanks for helping."},
        {"role": "user", "content": "Who is the first president of United States?"}
    ]
    }

    while True:
        response = requests.post(API_ENDPOINT, headers=HEADERS, json=payload)
        if response.status_code != 200:
            error_data = json.loads(response.text)
            print("Error:", error_data['error']['message'])
            break

        data = json.loads(response.text)
        reply = data['choices'][0]['message']['content']
        print("ChatGPT's reply:", reply)

        user_input = input("Your message: ")
        if 'bye' in user_input.lower():
            break

        payload['messages'].append({"role": "user", "content": user_input})

        time.sleep(2)  # Rate limiting

chat_with_gpt()