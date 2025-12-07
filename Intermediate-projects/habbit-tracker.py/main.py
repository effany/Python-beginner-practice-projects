import requests
import os
from dotenv import load_dotenv
load_dotenv()
from datetime import datetime

USERNAME = "effany"
TOKEN = os.environ.get("TOKEN")
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": "effany",
    "agreeTermsOfService": "yes", 
    "notMinor": "yes"

}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID, 
    "name": "French Study",
    "unit": "Hour",
    "type": "int", 
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}


# graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

# print(graph_response.text)

# our graph here https://pixe.la/v1/users/effany/graphs/graph1.html

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
# today = datetime.now()
today = datetime(year=2025, month=12, day=6)

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "4", 
}

# pixel_response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)

# print(pixel_response.text)

## update pixel 

date_to_update = datetime(year=2025, month=12, day=6).strftime("%Y%m%d")

pixel_update_enpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date_to_update}"

update_config = {
    "quantity": "8"
}

# update_response = requests.put(url=pixel_update_enpoint, json=update_config, headers=headers)

# print(update_response.text)

# delete pixel 
date_to_delete = datetime(year=2025, month=12, day=7).strftime("%Y%m%d")
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date_to_delete}"

delete_response = requests.delete(url=delete_endpoint, headers=headers)

print(delete_response.text)