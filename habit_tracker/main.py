# View the website: https://pixe.la/v1/users/uddeepta/graphs/graph1.html
import requests
from datetime import datetime

TOKEN = "tlksae53eanmxe"
USERNAME = "uddeepta"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

headers ={
    "X-USER-TOKEN": TOKEN,
}

# Use the following only to sign up / setting up a user account
# response = requests.post(url=pixela_endpoint, json=user_params)


# Use the following to create a graph
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# graph_config = {
#     "id": GRAPH_ID,
#     "name": "work hours",
#     "unit": "hours",
#     "type": "float",
#     "color": "ajisai",
# }

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

# Use the following to add a pixel
post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now()
post_pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you work today? : "),
}
response = requests.post(url=post_pixel_endpoint, json=post_pixel_params, headers=headers)


# Use the following to update a pixel
# update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20221017"
# pixel_update_params = {
#     "quantity": '0.0'
# }
# response = requests.put(url=update_pixel_endpoint, json=pixel_update_params, headers=headers)


# Use the following to delete a pixel
# pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20221018"
# response = requests.delete(url=pixel_delete_endpoint, headers=headers)


print(response.text)