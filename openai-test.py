# to install openai, run the terminal
# enter: pip install --upgrade openai
# to run the program, enter: python openai-test.py
# to exit the program, press ctrl + c

import os
from openai import OpenAI

OpenAI.api_key = ('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')
client = OpenAI(api_key="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")

user_input = "Produce: Coffee Quantity: 1 Expiry Date: 3 days Produce:Rice  Quantity: 2 Expiry Date: 3 days"

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "i have these expiring ingredients, please try to utilize all of them in a recipe and minimize the use of other ingredients as much as you can" + user_input},
  ]
)

print(completion.choices[0].message)