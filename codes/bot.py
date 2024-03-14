import csv
from flask import Flask, render_template, request
from nltk.chat.util import Chat, reflections

app = Flask(__name__)

# Load patterns and responses from CSV file
patterns = []
responses = []

with open('responses.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        patterns.append((row['Pattern'], row['Response'].split('|')))

# Create a chatbot using the loaded patterns
college_chatbot = Chat(patterns, reflections)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    response = college_chatbot.respond(user_input)
    return {'response': response}

if __name__ == "__main__":
    app.run(debug=True)