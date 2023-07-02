import requests
from create import imageURL
import os
import datetime

base_name = "image"

timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

new_filename = f"{base_name}_{timestamp}.png"


def save_image_from_url(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"Image saved successfully at: {save_path}")
    else:
        print(f"Failed to download image. Status code: {response.status_code}")

image_url = imageURL
save_location = f'images/{new_filename}'

save_image_from_url(image_url, save_location)


print(f"Image saved as: {new_filename}")