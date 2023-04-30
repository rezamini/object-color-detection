import requests

class ApiCalls:
    def __init__(self):
        pass

    def get_data(self):
        api_url = "https://jsonplaceholder.typicode.com/todos/1"
        response = requests.get(api_url)
        print("***** API GETTING RESULT *******")
        print(response.json())

    def send_data(self, data):
        api_url = "https://jsonplaceholder.typicode.com/todos"
        todo = {"userId": 1, "title": "Buy milk", "completed": False}
        response = requests.post(api_url, json=todo)
        print("***** API SENDING RESULT *******")
        print(response.json())
        print(response.status_code)
