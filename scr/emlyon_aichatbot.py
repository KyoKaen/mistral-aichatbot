import os
from mistralai import Mistral

api_key = os.environ["MISTRAL_API_KEY"]
model = "mistral-large-latest"

client = Mistral(api_key=api_key)

# Data to be injected
data = """ Admission Requirements: You need a minimum of a Bachelor's Degree, at least 3 years of work experience, GMAT, GRE, or TAGE MAGE scores, English proficiency scores, and 2 professional recommendation letters. Tuition Fees: The tuition fee for the International MBA program is €43,500 for the September 2025 intake. ... """ 
# Add all your collected data here

chat_response = client.chat.complete(
    model= model,
    messages = [
        {
            "role": "user",
            "content": "What is tuition fee of this MBA?",
        },
        {"role": "system", "content": "This is the EMLyon MBA application information: " + data},
        {"role": "system", "content": "Use the following information to answer any questions related to EMLyon's MBA program."}

    ]
)
print(chat_response.choices[0].message.content)



# prompt
# System Role: Provides the context or instructions for the AI model based on your collected data.
# question:
# User Role: Represents the questions from the users.
# answer:
# Assistant Role: Represents the answers to those user questions.
