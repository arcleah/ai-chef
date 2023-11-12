# to install openai, run the terminal
# enter: pip install --upgrade openai
# to run the program, enter: python openai-test.py
# to exit the program, press ctrl + c

from Flask import Flask, request,render_template
from openai import OpenAI

OpenAI.api_key = ('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')
client = OpenAI(api_key="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")

@app.route('/submit-data', methods=['POST'])
def submit_data():
  items_data = request.form['itemsData']
    
    # Construct the prompt for the OpenAI API
  prompt = f"You are a professional chef, skilled in creating recipes. I want you to make 3 at a time. I have limited ingredients and I want to make a delicious meal. In my pantry, I only have {items_data}. Can you give me options on various detailed recipes I can make with these ingredients? Please ensure to make use of listing the times needed for each step, the measurements, the estimated time it will take to cook the meal."
  return render_template("aboutus.html")
    # Call the OpenAI API with the prompt
    # ... OpenAI API call ...

    # Process the response and return/render as needed
    # ...


user_input = "Produce: Coffee Quantity: 1 Expiry Date: 3 days Produce:Rice  Quantity: 2 Expiry Date: 3 days"

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "i have these expiring ingredients, please try to utilize all of them in a recipe and minimize the use of other ingredients as much as you can" + user_input},
  ]
)

print(completion.choices[0].message)