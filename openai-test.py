# to install openai, run the terminal
# enter: pip install --upgrade openai
# to run the program, enter: python openai-test.py
# to exit the program, press ctrl + c

import os
from openai import OpenAI

OpenAI.api_key = ('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')
client = OpenAI(api_key="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")

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a professional chef, skilled in creating recipes. I have limited ingredients and I want to make a delicious meal, I only have eggs, carrots, striploin, and mushrooms. Can you give me options on various recipes I can make with these ingredients?"},
  ]
)

print(completion.choices[0].message)