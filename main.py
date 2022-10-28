"""
This code allows user to track their habits on Pixela.
NOTE: Remember to uncomment/comment on the relevant responses.
"""
import os
from datetime import datetime
import requests

START = input("""
Would you like to:
1 - Post a pixel
2 - Update a pixel
3 - Delete a pixel
""")

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
# delete_graph_response = requests.delete(
#     url=f"{GRAPH_ENDPOINT}/{GRAPH_ID}",
#     json=GRAPH_CONFIG,
#     headers=HEADERS
# )
# print(delete_graph_response.text)

# ------------------- POST A PIXEL ------------------- #
if START == "1":
    POST_PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

    quantity = input("How many times did you perform Salah today?\n")

    POST_PIXEL_CONFIG = {
        "date": TODAY,
        "quantity": quantity,
    }

    post_pixel_response = requests.post(
        url=POST_PIXEL_ENDPOINT,
        json=POST_PIXEL_CONFIG,
        headers=HEADERS
    )
    print(post_pixel_response.text)

# ------------------- UPDATE A PIXEL ------------------- #
if START == "2":
    UPDATE_PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{TODAY}"

    quantity = input("How many times did you perform Salah today?\n")

    UPDATE_PIXEL_CONFIG = {
        "quantity": quantity,
    }

    update_pixel_response = requests.put(
        url=UPDATE_PIXEL_ENDPOINT,
        json=UPDATE_PIXEL_CONFIG,
        headers=HEADERS
    )
    print(update_pixel_response.text)

# ------------------- DELETE A PIXEL ------------------- #
if START == "3":
    delete_date = input("Enter date to delete:\n(yyyyMMdd)\n")
    DELETE_PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{delete_date}"

    delete_pixel_response = requests.delete(url=DELETE_PIXEL_ENDPOINT, headers=HEADERS)
    print(delete_pixel_response.text)
