import os
from mistralai import Mistral
import json

# Set up API key
api_key = os.getenv("MISTRAL_API_KEY")
# api_key = os.environ["MISTRAL_API_KEY"]
model = "mistral-large-latest"
client = Mistral(api_key=api_key)

# Read the prompt from file
with open('../data/prompt.txt', 'r') as file:
    prompt = file.read()

# Read the sample data from file
with open('../data/sample_data.txt', 'r') as file:
    data = file.read()

# Read the test question from file
with open('../data/question_list.json', 'r') as file:
    question = json.load(file)
    print("***question0=" + str(question[0]))

# Inject data and train the model
# response = client.fine_tune(
#     model=model,
#     data={
#         "prompt": prompt,
#         "inputs": [
#             {"role": "system", "content": "This is the EMLyon MBA application information: " + data},
#             {"role": "system", "content": "Use the following information to answer any questions related to EMLyon's MBA program."},
#             question[0] # Test question
#         ],
#     }
# )
# print(response)

# Example query to test the model
response = client.chat.complete(
    model=model,
    messages=[
        question[0],
        {"role": "system", "content": "This is the EMLyon MBA application information: " + data},
        {"role": "system", "content": "Use the following information to answer any questions related to EMLyon's MBA program."}
    ]
)
print(response.choices[0].message.content)
