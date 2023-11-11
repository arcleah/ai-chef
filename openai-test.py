// to install openai, run the terminal
// enter: pip install --upgrade openai
// to run the program, enter: python openai-test.py
// to exit the program, press ctrl + c

import os
from openai import OpenAI

OpenAI.api_key = ('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')
client = OpenAI(api_key="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")

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)