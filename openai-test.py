# to install openai, run the terminal
# enter: pip install --upgrade openai
# to run the program, enter: python openai-test.py
# to exit the program, press ctrl + c

from flask import Flask, request, render_template, jsonify
from openai import OpenAI

OpenAI.api_key = ('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')
client = OpenAI(api_key="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")

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a professional chef, skilled in creating recipes. I want you to make 3 at a time: 1 focused on my preferences, and 2 which can stray a bit from it. I have limited ingredients and I want to make a delicious meal. In my pantry, I only have [2 carrots and 2 tomatoes]. Can you give me options on various detailed recipes I can make with these ingredients? Please ensure to make use of listing the times needed for each step, the measurements (as an example, sear the steak for 2 mins on each side, boil the potatoes for 10 mins, etc), the estimated time it will take to cook the meal (i.e. overall time is 30 mins, 1 hour, etc). please format it with the name of the recipe attached with the estimated time to prepare, followed by the list of ingredients and the amount needed, followed by the steps and make them detailed by including the amount of ingredients and time needed for each step."}
  ]
)

print(completion.choices[0].message)