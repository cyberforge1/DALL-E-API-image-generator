# create.py

import os

import openai

from randomizedGeneratorMerged import image_prompt
from dotenv import load_dotenv

load_dotenv()


PROMPT = image_prompt

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Image.create(
    prompt=PROMPT,
    n=1,
    size="256x256",
)

imageURL = response["data"][0]["url"]

print(response["data"][0]["url"])