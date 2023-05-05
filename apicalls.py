import requests

class ApiCalls:
    API_URL ="http://localhost:8888/smemAttributes"

    def __init__(self):
        pass

    def get_data(self):
        api_url = self.API_URL
        response = requests.get(api_url)
        print("***** API GETTING RESULT *******")
        print(response.json())
    
    def send_data(self, colorResult):
        api_url = self.API_URL

        attributes = {
            "color": list(colorResult)
        }

        payload = {"name": "detected_colors", "attributes":  attributes }
        # print(payload)
        
        response = requests.post(api_url, json=payload)
        print("***** API SENDING RESULT *******")
        print(response.json())
        print(response.status_code)
        print(response.ok)
