from flask import Flask

import google.generativeai as genai

genai.configure(api_key="AIzaSyBBR0qn28t8KtMFUZ5j_Dwj5MAl1BH4wfw")

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  }
]

model = genai.GenerativeModel(model_name="gemini-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

prompt_greeting = [
  "input: nama kamu adalah",
  "output: bubuy",
  "input: Bos kamu adalah",
  "output: Fitriyadi",
  "input: fitriyadi punya anak",
  "output: keenan dan yumna",
]

# response = model.generate_content(prompt_parts)
# print(response.text)


app = Flask(__name__)

@app.route("/AI/<ask>")
def appAsk(ask):

    prompt_parts = list(prompt_greeting)
    input = {"text": "input: " + ask}
    output = {"text": "output :"}
    prompt_parts.append(input)
    prompt_parts.append(output)

    response = model.generate_content(prompt_parts)
    return f"{response.text}"

@app.route("/AI/IQRO/<ask>")
def appLearn(ask):

    keywords = "IQRO"
    keyword = ask.split(":")

    if keyword[0] == keywords:
        print("belajar ap gan")
        input = {"text": "input: " + keyword[1]}
        output = {"text": "output: " + keyword[2]}
        prompt_greeting.append(input)
        prompt_greeting.append(output)

    return f"{prompt_greeting}"