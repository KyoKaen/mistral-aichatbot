# mistral-aichatbot


Sure! Here's a complete `README.md` for your project that you can copy and paste:

```markdown
# EMlyon MBA Chatbot

## Project Description
This project is an AI chatbot designed to answer queries related to the MBA program at EMlyon Business School using Mistral's API.

## Folder Structure
```plaintext
emlyon-mba-chatbot/
├── data/
│   ├── prompt.txt
│   ├── question_list.json
├── src/
│   ├── train_chatbot.py
├── README.md
├── requirements.txt
```

## Getting Started

### Prerequisites
- Python 3.x
- Mistral API key

### Installation
1. **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd emlyon-mba-chatbot
    ```

2. **Set up a virtual environment and install dependencies:**
    ```bash
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. **Obtain your Mistral API key and set it in your environment:**
    ```bash
    export MISTRAL_API_KEY='your_api_key'
    ```

### Folder Structure
- **`data/`**: Contains the `prompt.txt` and `question_list.json` files.
- **`src/`**: Contains the `train_chatbot.py` script.

### Files Description
- **`data/prompt.txt`**: Stores the prompt for the chatbot.
- **`data/question_list.json`**: Contains the list of questions and answers.
- **`src/train_chatbot.py`**: Python script to train and deploy the AI chatbot using Mistral's API.

## Steps to Run the Project
1. **Prepare the Data:**
    - Store the prompt in `data/prompt.txt`.
    - Store the question list and answers in `data/question_list.json`.

2. **Train and Deploy the Chatbot:**
    ```bash
    python src/train_chatbot.py
    ```

3. **Test the Chatbot:**
    - Use the example query in `train_chatbot.py` to test the chatbot.

## Example Query
You can test the chatbot using an example query:
```python
# Example query to test the model
query = "What are the admission requirements?"
response = client.generate(
    model=model,
    prompt="User: " + query + "\nAssistant:"
)
print(response)
```

## Contributing
1. Fork the project repository.
2. Create a feature branch: `git checkout -b feature/feature-name`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/feature-name`
5. Open a pull request.

## License
This project is licensed under the MIT License.
```

Copy and paste the content into your `README.md` file. This should help guide anyone through setting up and running the project. Does this work for you, or do you need any more adjustments? 😊

