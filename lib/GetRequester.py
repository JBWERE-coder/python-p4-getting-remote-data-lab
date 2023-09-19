import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.text
        else:
            return None

    def load_json(self):
       response_body = self.get_response_body()
       if response_body:
            try:
                json_data = json.loads(response_body)
                return json_data
            except json.JSONDecodeError:
                return None
       else:
            return None
        
if __name__ == "__main__":
    url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
    requester = GetRequester(url)
    json_data = requester.load_json()

    if json_data:
        # Now you can work with the loaded JSON data
        print(json_data)