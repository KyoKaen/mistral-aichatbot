import os
from mistralai import Mistral
import json

api_key = os.environ["MISTRAL_API_KEY"]
agent_id = "ag:95ecd8a8:20250107:emlyon-mba-ai-chatbot:0b66984f"

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
    # print("***question0=" + str(question[0]))

# print("*****agent_id=" + agent_id),
chat_response = client.agents.complete(
    agent_id=agent_id,
    messages=[
        {
            "role": "user",
            "content": "What is the MBA tuition fee?",
        },
    ],
    # trained only once
    # messages=[
    #     question[0],
    #     {"role": "system", "content": "This is the EMLyon MBA application information: " + data},
    #     {"role": "system", "content": "Use the following information to answer any questions related to EMLyon's MBA program."}
    # ],
)
print(chat_response.choices[0].message.content)
