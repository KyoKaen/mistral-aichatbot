import os
from mistralai import Mistral
from dotenv import load_dotenv
import os
import json

# Set up API key
# api_key = os.environ["MISTRAL_API_KEY"]
load_dotenv()
api_key = os.getenv("MISTRAL_API_KEY")
model = "mistral-large-latest"
client = Mistral(api_key=api_key)

# Read the prompt from file
with open('../data/prompt.txt', 'r') as file:
    prompt = file.read()

# Read the question list from file
with open('../data/question_list.json', 'r') as file:
    question_list = json.load(file)

# Train and inject data into the model
response = client.train_model(
    model=model,
    prompt=prompt,
    inputs=question_list
)
print(response)

# Example query to test the model
query = "What are the admission requirements?"
response = client.generate(
    model=model,
    prompt="User: " + query + "\nAssistant:"
)
print(response)

