import os
import openai
import markdownify

from env import *

openai.organization = OrganizationID
openai.api_key = APIKeySecret
#openai.api_key = os.getenv(APIKeySecret)

system_message = input("Enter software name : ")
system_user = input("Question : ")

print("------------------------------")

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": "Tu es un expert " + system_message
        },
        {
            "role": "user",
            "content": system_user
        },
    ]
)

response = response["choices"][0]["message"]["content"].replace("'", '"')
md = markdownify.markdownify(response)
print(md)
