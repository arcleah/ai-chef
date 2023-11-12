# to install openai, run the terminal
# enter: pip install --upgrade openai
# to run the program, enter: python openai-test.py
# to exit the program, press ctrl + c

from flask import Flask, request, render_template
from openai import OpenAI

OpenAI.api_key = ('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')
client = OpenAI(api_key="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")

@app.route('/submit-data', methods=['POST'])
def submit_data():
    items_data = request.form.get('itemsData')

    prompt = f"You are a professional chef, skilled in creating recipes. I want you to make 3 at a time. I have limited ingredients and I want to make a delicious meal. In my pantry, I only have {items_data}. Can you give me options on various detailed recipes I can make with these ingredients?
              Please ensure to make use of listing the times needed for each step, the measurements (as an example, 
              'sear the steak for 2 mins on each side', 'boil the potatoes for 10 mins', etc), the estimated time 
              it will take to cook the meal (i.e. 'overall time is 30 mins', 1 hour, etc). Please format it with the 
              name of the recipe attached with the estimated time to prepare, followed by the list of ingredients and 
              the amount needed, followed by the steps and make them detailed by including the amount of ingredients 
              and time needed for each step"

    response = openai.Completion.create(
        model="gpt-3.5-turbo",  # Replace with the model you want to use
        prompt=prompt,
        max_tokens=150
    )

    recipe = response.choices[0].text.strip()
    return render_template("aboutus.html", recipe=recipe)  # Pass the recipe to the template

if __name__ == '__main__':
    app.run(debug=True)