"""
This code allows user to track their habits on Pixela.
NOTE: Remember to uncomment/comment on the relevant responses.
"""
import os
from datetime import datetime
import requests

QUANTITY = input("How many times did you perform Salah today?\n")

TODAY = datetime.now().strftime("%Y%m%d")
USERNAME = "zoul"
TOKEN = os.environ.get("TOKEN")
GRAPH_ID = "salah5"

HEADERS = {
    "X-USER-TOKEN": TOKEN
}

# ------------------- CREATE NEW USER ------------------- #
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USER_PARAMS = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# pixela_response = requests.post(url=PIXELA_ENDPOINT, json=USER_PARAMS)
# print(pixela_response.text)

# ------------------- CREATE NEW GRAPH ------------------- #
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
GRAPH_CONFIG = {
    "id": GRAPH_ID,
    "name": "Salah Tracker",
    "unit": "salah",
    "type": "int",
    "color": "ajisai",
    "timezone": "Singapore"
}

# graph_response = requests.post(url=GRAPH_ENDPOINT, json=GRAPH_CONFIG, headers=HEADERS)
# print(graph_response.text)

# ------------------- DELETE GRAPH ------------------- #
# delete_graph_response = requests.delete(url=f"{GRAPH_ENDPOINT}/{GRAPH_ID}", json=GRAPH_CONFIG, headers=HEADERS)
# print(delete_graph_response.text)

# ------------------- POST A PIXEL ------------------- #
POST_PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
POST_PIXEL_CONFIG = {
    "date": TODAY,
    "quantity": QUANTITY,
}

post_pixel_response = requests.post(
    url=POST_PIXEL_ENDPOINT,
    json=POST_PIXEL_CONFIG,
    headers=HEADERS
)
print(post_pixel_response.text)

# ------------------- UPDATE A PIXEL ------------------- #
UPDATE_PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/<yyyyMMdd>"
UPDATE_PIXEL_CONFIG = {
    "quantity": QUANTITY,
}

# update_pixel_response = requests.put(
#     url=UPDATE_PIXEL_ENDPOINT,
#     json=UPDATE_PIXEL_CONFIG,
#     headers=HEADERS
# )
# print(update_pixel_response.text)

# ------------------- DELETE A PIXEL ------------------- #
DELETE_PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/<yyyyMMdd>"

# delete_pixel_response = requests.delete(url=DELETE_PIXEL_ENDPOINT, headers=HEADERS)
# print(delete_pixel_response.text)
